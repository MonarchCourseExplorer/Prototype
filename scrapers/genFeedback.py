import sys
import psycopg2
from catalogue_scraper import createConnection
import csv

def courseOutput(conn):
    strSQL = """SELECT number, name, COUNT(*) as num_sections 
        FROM catalogue_course AS course INNER JOIN catalogue_section AS section on course.id = section.course_id 
        WHERE semester = '202310' AND department = 'CS' AND number SIMILAR TO '[1234]%' 
        GROUP BY number, name"""

    output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(strSQL)

    cur = conn.cursor()
    with open('courses.csv', 'w') as f:
        cur.copy_expert(output, f)

def feedbackInput(conn):
    disclaimer = "This feedback was artificially generated, and has no relation to real life.\n"
    #Select the sections for the given semester and course, and assign a row number
    rowSelect = """SELECT section.semester, course.id AS course_id, section.id AS section_id, ROW_NUMBER() OVER (ORDER BY section.id) AS row_num
        FROM catalogue_course AS course INNER JOIN catalogue_section AS section on course.id = section.course_id 
        WHERE semester = %(sem)s AND department = %(dep)s AND number = %(num)s """
    #select a random number between 1 and the number of sections for a given course and semester
    rowCount = "SELECT semester, course_id, trunc(random() * COUNT(*)) + 1 AS rand_row FROM catalogue_section GROUP BY semester, course_id "
    #Insert sections where the row number matches a random number. Select only the first match
    insertSQL = """INSERT INTO catalogue_feedback (section_id, difficulty_rating, openness_rating, workload_rating, review)
        SELECT sections.section_id, %(rating)s, %(rating)s, %(rating)s, %(review)s
        FROM ({0}) AS sections INNER JOIN ({1}) AS section_count ON sections.semester = section_count.semester AND sections.course_id = section_count.course_id 
        WHERE sections.row_num = section_count.rand_row;""".format(rowSelect, rowCount)

    semester = "202310"
    cur = conn.cursor()
    with open('feedback.csv', 'r') as f:
        fbreader = csv.reader(f, dialect='excel')
        for row in fbreader:
            #read the row
            department = row[0]
            number = row[1]
            rating = row[2]
            feedback = row[3]

            if department != "department":
                #randomly assign the feedback to a section within that course
                cur.execute(insertSQL, {'sem': semester, 'dep': department, 'num': number, 'rating': rating, 'review': disclaimer + feedback})
                conn.commit()


if __name__ == "__main__":
    conn = createConnection()

    if conn != None:
        
        if sys.argv[0] == "output":
            courseOutput(conn)
        else:
            feedbackInput(conn)

        conn.close()
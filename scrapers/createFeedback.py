from dataclasses import dataclass
import csv
import subprocess
import sys

@dataclass
class Course:
    department = "CS"
    number = ""
    name = ""
    count = 0

if __name__ == "__main__":
    #load courses from csv
    courses = []
    with open('courses.csv', 'r') as f:
        coursereader = csv.reader(f, dialect='excel')
        for row in coursereader:
            if row[0] != "number":
                c = Course()

                c.number = row[0].strip()
                c.name = row[1]
                c.count = int(row[2])
                courses.append(c)

    ratings = ["1 star", "2 stars", "3 stars", "4 stars", "5 stars"]

    llamaPath = "/home/davidj/Documents/cs410/llama.cpp/main"
    modelPath = "/home/davidj/Documents/cs410/llama.cpp/models/llama-2-13b.Q5_K_M.gguf"

    with open('feedback.csv', 'a') as f:
        fbwriter = csv.writer(f, dialect='excel')
        fbwriter.writerow(["department", "number", "rating", "feedback"])

        for course in courses:
            print(course.number)
            for rating in ratings:
                prompt = "You are a student at ODU. Please give some feedback on the course \"{1}\", similar to RateMyProfessor.com. Include how hard it was, if the textbook was useful, and how the professor taught. You rated this course {0} out of 5.\nFeedback: ".format(rating, course.name)
                for i in range(course.count):                    
                    result = subprocess.run([llamaPath, "-m", modelPath, "-p", prompt, "-n", "200", "-e", "-c", "2048"], capture_output=True, text=True)
                    fbwriter.writerow([course.department, course.number, rating[:1], result.stdout[len(prompt):]])
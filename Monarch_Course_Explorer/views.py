from django.shortcuts import render

# Render the Monarch Course Explorer home page
def homeView(request):
    return render(request, 'index.html')

# Render gallery page
def galleryView(request):
    return render(request, 'pages/gallery.html')

# Render the portfolio page
def portfolioView(request):
    return render(request, 'pages/portfolio.html')

# Render the full width page
def fullWidthView(request):
    return render(request, 'pages/full-width.html')

# Render the sidebar-left page
def sidebarLeftView(request):
    return render(request, 'pages/sidebar-left.html')

# Render the sidebar-left 2 page
def sidebarLeftView2(request):
    return render(request, 'pages/sidebar-left-2.html')

# Render the sidebar-right page
def sidebarRightView(request):
    return render(request, 'pages/sidebar-right.html')

# Render the sidebar-right 2 page
def sidebarRightView2(request):
    return render(request, 'pages/sidebar-right-2.html')

# Render the basic-grid page
def basicGridView(request):
    return render(request, 'pages/basic-grid.html')

def provideFeedbackView(request):
    return render(request, 'pages/provideFeedback.html')
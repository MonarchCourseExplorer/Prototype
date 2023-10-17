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

# Render the sidebar left page
def sidebarLeftView(request):
    return render(request, 'pages/sidebar-left.html')


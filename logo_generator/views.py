# logo_generator/views.py
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from .utils import generate_custom_logo, get_canva_auth_url, fetch_canva_tokens, fetch_canva_templates, import_canva_design, import_canva_template
def home(request):
    # Example view to render home page template
    return render(request, 'home.html')

def fetch_templates(request):
    # Example view to fetch Canva templates
    try:
        templates = fetch_canva_templates()
        return HttpResponse(f"Templates: {templates}")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def import_template(request, template_id):
    # Example view to import a Canva template
    try:
        response = import_canva_template(template_id)
        return HttpResponse(f"Template imported: {response}")
    except Exception as e:
        return HttpResponse(f"Error importing template: {str(e)}")

def create_logo(request):
    if request.method == 'POST':
        color_choice = request.POST.get('color_choice')
        text_input = request.POST.get('text_input')
        shape_choice = request.POST.get('shape_choice')
        
        # Generate custom logo using utils function
        logo_image = generate_custom_logo(color_choice, text_input, shape_choice)

        # Return logo as response (example: in HTTP response)
        response = HttpResponse(content_type='image/png')
        logo_image.save(response, format='PNG')
        return response
    else:
        # Handle GET request to show form for logo creation
        return render(request, 'logo_form.html')

def canva_auth(request):
    redirect_uri = request.build_absolute_uri('/canva/callback/')
    auth_url = get_canva_auth_url(redirect_uri)
    return redirect(auth_url)

def canva_callback(request):
    code = request.GET.get('code')
    redirect_uri = request.build_absolute_uri('/canva/callback/')
    token = fetch_canva_tokens(code, redirect_uri)
    # Save token securely (e.g., in session or database)
    return render(request, 'canva_callback.html', {'token': token})

def fetch_templates(request):
    # Retrieve access token from session or database
    access_token = request.session.get('canva_access_token')
    templates = fetch_canva_templates(access_token)
    return render(request, 'templates.html', {'templates': templates})

def import_design(request, template_id):
    # Retrieve access token from session or database
    access_token = request.session.get('canva_access_token')
    design_data = import_canva_design(access_token, template_id)
    return render(request, 'import_design.html', {'design_data': design_data})
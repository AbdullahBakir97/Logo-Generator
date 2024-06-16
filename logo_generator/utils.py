# logo_generator/utils.py
from PIL import Image, ImageDraw, ImageFont
import requests
from requests_oauthlib import OAuth2Session
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

def get_canva_auth_url(redirect_uri):
    authorization_base_url = settings.CANVA_API_BASE_URL + '/oauth/authorize'
    canva = OAuth2Session(settings.CANVA_CLIENT_ID, redirect_uri=redirect_uri)
    authorization_url, state = canva.authorization_url(authorization_base_url)
    return authorization_url

def fetch_canva_tokens(code, redirect_uri):
    token_url = settings.CANVA_API_BASE_URL + '/oauth/token'
    canva = OAuth2Session(settings.CANVA_CLIENT_ID, redirect_uri=redirect_uri)
    token = canva.fetch_token(token_url, code=code, client_secret=settings.CANVA_CLIENT_SECRET)
    return token

def authenticate_canva_api():
    # Placeholder for Canva API OAuth2 authentication flow
    pass


def fetch_canva_templates(access_token):
    url = settings.CANVA_API_BASE_URL + '/v1/templates'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise exception for bad responses
    templates = response.json()
    return templates

def import_canva_template(template_id):
    try:
        url = f'https://api.canva.com/v1/templates/{template_id}/import'
        # Implement logic to import the template
        # Example: Make a POST request to import the template
        response = requests.post(url, headers={'Authorization': f'Bearer {settings.CANVA_API_KEY}'})
        response.raise_for_status()  # Raise exception for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error importing Canva template {template_id}: {str(e)}")
        raise
    
def import_canva_design(access_token, template_id):
    url = settings.CANVA_API_BASE_URL + f'/v1/templates/{template_id}/import'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers)
    response.raise_for_status()  # Raise exception for bad responses
    design_data = response.json()
    return design_data


def generate_custom_logo(color_choice, text_input, shape_choice):
    # Example custom logo generation with Pillow
    img = Image.new('RGB', (500, 500), color=color_choice)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", size=36)
    draw.text((10, 10), text_input, font=font, fill="white")
    # Draw shapes based on shape_choice (example: rectangle)
    if shape_choice == 'rectangle':
        draw.rectangle([(100, 100), (400, 400)], outline='black', width=2)
    # Save or return the image
    return img

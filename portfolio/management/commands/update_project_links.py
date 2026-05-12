"""
Django management command to update project links (remove fake/generic links)
Run with: python manage.py update_project_links
"""
from django.core.management.base import BaseCommand
from portfolio.models import Project


class Command(BaseCommand):
    help = 'Update project links - remove generic GitHub links and add confidentiality notes'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Updating project links...'))
        
        # Update Royal Soft company projects - remove all links
        company_projects = [
            'intelligent-erp-chatbot',
            'ai-php-code-generation',
            'sdlc-automation-bot'
        ]
        
        for slug in company_projects:
            try:
                project = Project.objects.get(slug=slug)
                project.github_url = ''
                project.live_url = ''
                
                # Add confidentiality note to description if not already present
                if 'Internal Royal Soft production project' not in project.description:
                    project.description = f"{project.description} [Internal Royal Soft production project]"
                
                # Add note to full description
                if 'confidentiality' not in project.full_description.lower():
                    project.full_description += "\n\nNote: This is an internal company production project. Public live link is not available due to confidentiality."
                
                project.save()
                self.stdout.write(self.style.SUCCESS(f'✅ Updated: {project.title}'))
            except Project.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'⚠ Project not found: {slug}'))
        
        # Update E-Commerce project - keep live link, remove generic GitHub
        try:
            ecommerce = Project.objects.get(slug='ecommerce-recommendation-engine')
            ecommerce.github_url = ''
            ecommerce.live_url = 'https://abdul007.pythonanywhere.com'
            ecommerce.save()
            self.stdout.write(self.style.SUCCESS(f'✅ Updated: {ecommerce.title}'))
        except Project.DoesNotExist:
            self.stdout.write(self.style.WARNING('⚠ E-commerce project not found'))
        
        # Update other projects - remove generic GitHub links
        other_projects = ['diabetes-prediction-ml', 'employee-management-system']
        for slug in other_projects:
            try:
                project = Project.objects.get(slug=slug)
                project.github_url = ''
                project.live_url = ''
                project.save()
                self.stdout.write(self.style.SUCCESS(f'✅ Updated: {project.title}'))
            except Project.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'⚠ Project not found: {slug}'))
        
        self.stdout.write(self.style.SUCCESS('\n✅ All project links updated successfully!'))
        self.stdout.write(self.style.SUCCESS('Company projects now show as confidential without public links.'))

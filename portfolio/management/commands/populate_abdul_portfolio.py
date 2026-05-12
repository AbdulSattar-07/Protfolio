"""
Django management command to populate Abdul Sattar's portfolio data
Run with: python manage.py populate_abdul_portfolio
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from portfolio.models import (
    Profile, AboutStat, SkillCategory, Skill, ExperienceEntry,
    EducationEntry, Project, Category, Technology, Achievement,
    Certification, SiteSettings
)
from datetime import date

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate Abdul Sattar portfolio data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting portfolio population...'))
        
        # Create superuser if doesn't exist
        self.create_superuser()
        
        # Populate all sections
        self.populate_profile()
        self.populate_site_settings()
        self.populate_about_stats()
        self.populate_skills()
        self.populate_experience()
        self.populate_education()
        self.populate_categories_and_technologies()
        self.populate_projects()
        self.populate_achievements()
        self.populate_certifications()
        
        self.stdout.write(self.style.SUCCESS('✅ Portfolio populated successfully!'))
        self.stdout.write(self.style.SUCCESS('You can now run: python manage.py runserver'))
        self.stdout.write(self.style.SUCCESS('And access admin at: http://127.0.0.1:8000/admin/'))

    def create_superuser(self):
        """Create superuser for admin access"""
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='malikabdulsattar9947@gmail.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('✅ Superuser created (username: admin, password: admin123)'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Superuser already exists'))

    def populate_profile(self):
        """Populate Profile data"""
        profile, created = Profile.objects.get_or_create(
            id=1,
            defaults={
                'name': 'Abdul Sattar',
                'title': 'AI & ML Engineer | Python Developer | GenAI Specialist',
                'headline': 'Production AI Systems | GenAI & Multi-Agent Expert | Python & Django Developer',
                'location': 'Lahore, Pakistan',
                'email': 'malikabdulsattar9947@gmail.com',
                'phone': '+92 346 612 6667',
                'short_bio': 'AI & ML Engineer specializing in GenAI, RAG systems, multi-agent applications, Django APIs, and machine learning solutions.',
                'current_position': 'AI & ML Engineer at Royal Soft',
                'summary': '''I am an AI & ML Engineer and Python Developer with production experience in building GenAI systems, multi-agent architectures, RAG-based applications, ML-powered platforms, and Django REST API solutions. My work focuses on converting real business requirements into intelligent, production-ready systems using Python, LangChain, LangGraph, OpenAI APIs, ChromaDB, n8n, Scikit-learn, Django, and MySQL.

At Royal Soft, I worked on live enterprise AI systems including an ERP chatbot, an AI-powered PHP ERP code generation system, and an SDLC automation bot. These systems improved business query handling, reduced manual development effort, automated task planning, and connected AI workflows with real databases and REST APIs.

I also led the development of an AI-powered e-commerce recommendation platform as my final year project, combining collaborative filtering and content-based filtering to deliver personalized product recommendations.'''
            }
        )
        self.stdout.write(self.style.SUCCESS(f'✅ Profile {"created" if created else "updated"}'))

    def populate_site_settings(self):
        """Populate Site Settings"""
        settings, created = SiteSettings.objects.get_or_create(
            id=1,
            defaults={
                'site_name': 'Abdul Sattar - AI & ML Engineer',
                'site_description': 'AI & ML Engineer specializing in GenAI, RAG systems, multi-agent applications, Django APIs, and machine learning solutions.',
                'site_keywords': 'AI Engineer, ML Engineer, GenAI, RAG, LangChain, Django, Python Developer, Multi-Agent Systems',
                'contact_email': 'malikabdulsattar9947@gmail.com',
                'github_url': 'https://github.com/AbdulSattar-07',
                'linkedin_url': 'https://linkedin.com/in/abdul-sattar-a8179731a',
                'twitter_url': '',
                'kaggle_url': '',
                'whatsapp_url': 'https://wa.me/923466126667',
            }
        )
        self.stdout.write(self.style.SUCCESS(f'✅ Site Settings {"created" if created else "updated"}'))

    def populate_about_stats(self):
        """Populate About Stats / Counters"""
        stats_data = [
            {'number': '4', 'label': 'Production Systems', 'description': 'GenAI & ML Applications', 'order': 1},
            {'number': '1+', 'label': 'Year Experience', 'description': 'Production AI Engineering', 'order': 2},
            {'number': '500+', 'label': 'Daily Queries', 'description': 'ERP Chatbot Workload', 'order': 3},
            {'number': '3.78', 'label': 'CGPA', 'description': 'B.I.T Graduate', 'order': 4},
            {'number': '1400+', 'label': 'Code Files', 'description': 'Used in RAG Code Generation System', 'order': 5},
            {'number': '85%+', 'label': 'ML Precision', 'description': 'E-Commerce Recommendation Engine', 'order': 6},
        ]
        
        for stat_data in stats_data:
            AboutStat.objects.get_or_create(
                number=stat_data['number'],
                label=stat_data['label'],
                defaults=stat_data
            )
        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(stats_data)} About Stats'))

    def populate_skills(self):
        """Populate Skills with Categories"""
        skills_data = {
            'Core Language & Web': [
                ('Python', 92), ('SQL', 86), ('HTML5', 80), ('CSS3', 78)
            ],
            'AI / GenAI Engineering': [
                ('LangChain', 90), ('LangGraph', 86), ('RAG Systems', 90),
                ('OpenAI API', 86), ('n8n Workflow Automation', 84), ('NLP', 86),
                ('Prompt Engineering', 88), ('Multi-Agent Orchestration', 88),
                ('Intelligent Workflow Automation', 85)
            ],
            'ML Engineering': [
                ('Scikit-learn', 88), ('Predictive Modeling', 86), ('Feature Engineering', 85),
                ('Data Preprocessing', 87), ('Hyperparameter Tuning', 82), ('Cross-Validation', 84),
                ('ML Pipelines', 84), ('Dimensionality Reduction', 78), ('Anomaly Detection', 76),
                ('Model Evaluation', 86)
            ],
            'Web Frameworks & APIs': [
                ('Django', 88), ('Django REST APIs', 86), ('Django ORM & Auth', 84),
                ('Flask', 76), ('REST API Integration', 85), ('TMS API Integration', 82)
            ],
            'Data & Visualization': [
                ('Pandas', 90), ('NumPy', 88), ('Matplotlib', 84),
                ('Seaborn', 82), ('Plotly KPI Dashboards', 82)
            ],
            'Databases & Vector Stores': [
                ('MySQL', 86), ('SQL', 86), ('ChromaDB', 84),
                ('XAMPP', 76), ('Database Design & Normalization', 82)
            ],
            'Dev Tools': [
                ('Git', 84), ('GitHub', 85), ('Jupyter Notebook', 86),
                ('Google Colab', 84), ('VS Code', 88), ('PyCharm', 80)
            ],
            'Soft Skills': [
                ('Problem Solving', None), ('Self-Driven Learning', None),
                ('Technical Writing', None), ('Cross-Functional Collaboration', None)
            ]
        }
        
        order = 1
        for category_name, skills in skills_data.items():
            category, _ = SkillCategory.objects.get_or_create(
                name=category_name,
                defaults={'section': 'about', 'order': order}
            )
            order += 1
            
            skill_order = 1
            for skill_name, level in skills:
                Skill.objects.get_or_create(
                    category=category,
                    name=skill_name,
                    defaults={'level': level, 'order': skill_order}
                )
                skill_order += 1
        
        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(skills_data)} Skill Categories'))

    def populate_experience(self):
        """Populate Experience Entries"""
        experiences = [
            {
                'company': 'Royal Soft',
                'role': 'AI & ML Developer',
                'period': 'Aug 2025 – Mar 2026',
                'employment_type': 'Professional Experience',
                'description': 'Worked as an AI & ML Developer at Royal Soft, building production-grade GenAI and multi-agent systems for real enterprise use cases. Developed AI-powered ERP automation systems using Python, Django, LangChain, LangGraph, ChromaDB, OpenAI APIs, MySQL, n8n, and REST APIs.',
                'achievements': '''Architected a production-grade ERP chatbot using Python, Django, LangChain, and NLP for a live enterprise client processing 500+ daily natural-language business queries.
Integrated LangChain agents with live MySQL databases and REST APIs for inventory tracking, business Q&A, and real-time Plotly KPI dashboards.
Built an AI-powered PHP code generation system using RAG, LangGraph, and ChromaDB trained on 1,400+ company code files.
Achieved 70–90% similarity with the real ERP codebase in AI-generated PHP forms.
Reduced manual development effort by 60%+ through AI-assisted code generation.
Built an n8n-orchestrated SDLC Automation Bot using a 3-stage GPT-4o-mini pipeline.
Integrated TMS APIs for auto-assignment of development tasks and reduced project kick-off time by 60%+.''',
                'section': 'both',
                'order': 1
            },
            {
                'company': 'Islamia University of Bahawalpur',
                'role': 'AI Project Lead — Final Year Project',
                'period': 'Aug 2024 – Jun 2025',
                'employment_type': 'Academic Project Leadership',
                'description': 'Led the end-to-end development of a full-featured AI-powered e-commerce platform integrated with a hybrid product recommendation engine using collaborative filtering and content-based filtering.',
                'achievements': '''Led development of an AI-powered e-commerce platform with personalized product recommendations.
Built a hybrid recommendation engine using collaborative filtering and content-based filtering.
Achieved 85%+ recommendation precision on a held-out validation set.
Personalized product suggestions using user behaviour, purchase history, and item similarity.
Deployed the platform live on PythonAnywhere using Django and MySQL.
Optimized MySQL schema to support concurrent user sessions.''',
                'section': 'both',
                'order': 2
            },
            {
                'company': 'Code Lab Tech School & IT Solutions',
                'role': 'Python & ML Intern',
                'period': 'May 2023 – Sep 2023',
                'employment_type': 'Internship',
                'description': 'Completed structured training in Python, machine learning, data analysis, predictive modeling, data visualization, Django development, and MySQL integration.',
                'achievements': '''Completed training in data analysis using Pandas and NumPy.
Built predictive modeling projects using Scikit-learn.
Created visualizations using Matplotlib and Seaborn.
Built 3 functional data projects during the internship.
Delivered a working Django web application with MySQL integration as the capstone project.''',
                'section': 'both',
                'order': 3
            }
        ]
        
        for exp_data in experiences:
            ExperienceEntry.objects.get_or_create(
                company=exp_data['company'],
                role=exp_data['role'],
                defaults=exp_data
            )
        
        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(experiences)} Experience Entries'))

    def populate_education(self):
        """Populate Education Entries"""
        education = {
            'degree': 'Bachelor of Information Technology (B.I.T)',
            'institution': 'Islamia University of Bahawalpur, Pakistan',
            'period': '2021 – 2025',
            'grade': 'CGPA: 3.78 / 4.00',
            'highlights': '''Top 10% of Class
Data Structures
Machine Learning
Database Systems
Software Engineering
Web Technologies
Object-Oriented Programming''',
            'section': 'both',
            'order': 1
        }
        
        EducationEntry.objects.get_or_create(
            degree=education['degree'],
            institution=education['institution'],
            defaults=education
        )
        
        self.stdout.write(self.style.SUCCESS('✅ Created Education Entry'))

    def populate_categories_and_technologies(self):
        """Populate Project Categories and Technologies"""
        categories = [
            ('GenAI', 'genai', 'AI-powered generation systems'),
            ('RAG', 'rag', 'Retrieval-Augmented Generation'),
            ('NLP', 'nlp', 'Natural Language Processing'),
            ('Automation', 'automation', 'Workflow automation systems'),
            ('Production', 'production', 'Production-deployed systems'),
            ('AI/ML', 'ai-ml', 'Artificial Intelligence & Machine Learning'),
            ('E-commerce', 'e-commerce', 'E-commerce platforms'),
            ('Healthcare', 'healthcare', 'Healthcare applications'),
            ('Classification', 'classification', 'Classification models'),
            ('Web Development', 'web-development', 'Web development projects'),
            ('Django', 'django', 'Django framework projects'),
            ('HR System', 'hr-system', 'Human Resources systems'),
        ]
        
        for idx, (name, slug, desc) in enumerate(categories, 1):
            Category.objects.get_or_create(
                slug=slug,
                defaults={'name': name, 'description': desc, 'order': idx}
            )
        
        technologies = [
            ('Python', 'python', 'fab fa-python', 'text-blue-400', True),
            ('Django', 'django', 'fab fa-python', 'text-green-600', True),
            ('LangChain', 'langchain', 'fas fa-link', 'text-purple-500', True),
            ('LangGraph', 'langgraph', 'fas fa-project-diagram', 'text-indigo-500', True),
            ('OpenAI', 'openai', 'fas fa-brain', 'text-teal-500', True),
            ('ChromaDB', 'chromadb', 'fas fa-database', 'text-orange-500', False),
            ('MySQL', 'mysql', 'fas fa-database', 'text-blue-600', True),
            ('Scikit-learn', 'scikit-learn', 'fas fa-chart-line', 'text-orange-600', True),
            ('Pandas', 'pandas', 'fas fa-table', 'text-blue-500', False),
            ('NumPy', 'numpy', 'fas fa-calculator', 'text-blue-400', False),
            ('Plotly', 'plotly', 'fas fa-chart-bar', 'text-indigo-600', False),
            ('n8n', 'n8n', 'fas fa-cogs', 'text-red-500', False),
            ('REST API', 'rest-api', 'fas fa-exchange-alt', 'text-green-500', False),
            ('NLP', 'nlp', 'fas fa-language', 'text-purple-600', False),
            ('RAG', 'rag', 'fas fa-search', 'text-yellow-600', False),
            ('PHP', 'php', 'fab fa-php', 'text-indigo-700', False),
            ('JavaScript', 'javascript', 'fab fa-js', 'text-yellow-500', False),
            ('HTML/CSS', 'html-css', 'fab fa-html5', 'text-orange-600', False),
            ('Bootstrap', 'bootstrap', 'fab fa-bootstrap', 'text-purple-700', False),
            ('XGBoost', 'xgboost', 'fas fa-rocket', 'text-red-600', False),
            ('SMOTE', 'smote', 'fas fa-balance-scale', 'text-green-600', False),
            ('Matplotlib', 'matplotlib', 'fas fa-chart-area', 'text-blue-700', False),
            ('Seaborn', 'seaborn', 'fas fa-chart-pie', 'text-teal-600', False),
            ('Jupyter Notebook', 'jupyter', 'fas fa-book', 'text-orange-500', False),
        ]
        
        for idx, (name, slug, icon, color, featured) in enumerate(technologies, 1):
            Technology.objects.get_or_create(
                slug=slug,
                defaults={
                    'name': name,
                    'icon': icon,
                    'color': color,
                    'featured_on_home': featured,
                    'order': idx
                }
            )
        
        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(categories)} Categories and {len(technologies)} Technologies'))

    def populate_projects(self):
        """Populate Projects"""
        projects_data = [
            {
                'title': 'Intelligent ERP Chatbot — Multi-Agent System',
                'slug': 'intelligent-erp-chatbot',
                'description': 'Production-deployed multi-agent ERP chatbot for a live enterprise client, processing 500+ natural-language business queries per day with high accuracy.',
                'full_description': '''Built a production-deployed multi-agent ERP chatbot for a live enterprise client. The system processes 500+ natural-language business queries per day and uses LangChain agents to handle inventory tracking, business Q&A, and real-time KPI dashboard generation. It also supports memory-enabled conversation context for multi-turn business dialogues.''',
                'features': '''500+ daily business queries
Multi-agent orchestration
Inventory tracking
Business Q&A
Real-time Plotly KPI dashboards
Memory-enabled conversation context
Django production deployment
35% faster query resolution
Reduced manual lookup effort by around 40%''',
                'categories': ['GenAI', 'NLP', 'Production'],
                'technologies': ['Python', 'Django', 'LangChain', 'NLP', 'Plotly', 'MySQL'],
                'github_url': 'https://github.com/AbdulSattar-07',
                'live_url': '',
                'status': 'production',
                'featured': True,
                'year': '2025–2026',
                'rating': 5.0,
                'order': 1
            },
            {
                'title': 'AI-Powered Enterprise PHP Code Generation System',
                'slug': 'ai-php-code-generation',
                'description': 'Production multi-agent RAG pipeline that auto-generates enterprise PHP ERP forms including CRUD, AJAX, and database logic.',
                'full_description': '''Built an AI system to auto-generate enterprise PHP ERP forms using RAG and multi-agent architecture. The system retrieves real company code patterns from 1,400+ ERP code files and generates PHP forms aligned with the existing ERP codebase. The pipeline includes intent understanding, retrieval, LLM generation, validation, and production-ready output formatting.''',
                'features': '''RAG-based code generation
LangGraph multi-agent pipeline
ChromaDB vector storage
1,400+ company code files used for retrieval
PHP ERP form generation
CRUD + AJAX + DB logic generation
Intent → Retrieval → LLM → Validation pipeline
70–90% code similarity with real ERP codebase
60%+ reduction in manual development effort''',
                'categories': ['GenAI', 'RAG', 'Production'],
                'technologies': ['Python', 'Django', 'LangChain', 'LangGraph', 'ChromaDB', 'OpenAI', 'MySQL', 'PHP'],
                'github_url': 'https://github.com/AbdulSattar-07',
                'live_url': '',
                'status': 'production',
                'featured': True,
                'year': '2025–2026',
                'rating': 5.0,
                'order': 2
            },
            {
                'title': 'SDLC Automation Bot — AI-Powered Workflow Automation',
                'slug': 'sdlc-automation-bot',
                'description': 'Production n8n automation bot that converts meeting transcripts, PDFs, and SDLC documents into structured development task plans.',
                'full_description': '''Built a production-deployed SDLC Automation Bot using n8n. The system ingests meeting transcripts, PDFs, and SDLC documents, then converts unstructured input into structured developer task plans using a 3-stage GPT-4o-mini pipeline: Requirements, System Design, and Task Breakdown. It integrates with live TMS REST APIs for project matching, developer workload analysis, and automated task assignment.''',
                'features': '''Meeting transcript parsing
PDF and SDLC document ingestion
3-stage GPT-4o-mini pipeline
Requirements extraction
System design generation
Task breakdown generation
TMS REST API integration
Developer capacity analysis
Automated task assignment
60%+ faster project kick-off''',
                'categories': ['GenAI', 'Automation', 'Production'],
                'technologies': ['Python', 'n8n', 'OpenAI', 'JavaScript', 'REST API', 'HTML/CSS'],
                'github_url': 'https://github.com/AbdulSattar-07',
                'live_url': '',
                'status': 'production',
                'featured': True,
                'year': '2025–2026',
                'rating': 4.9,
                'order': 3
            },
            {
                'title': 'AI-Powered E-Commerce Recommendation Engine',
                'slug': 'ecommerce-recommendation-engine',
                'description': 'Full e-commerce platform integrated with a hybrid recommendation engine using collaborative and content-based filtering.',
                'full_description': '''Designed and developed a full e-commerce platform with an AI-powered product recommendation engine. The system uses hybrid filtering by combining collaborative filtering and content-based filtering. It personalizes product suggestions using user behaviour, purchase history, and item similarity.''',
                'features': '''Hybrid recommendation engine
Collaborative filtering
Content-based filtering
85%+ recommendation precision
User behaviour analysis
Purchase history-based suggestions
Item similarity matching
Django backend
MySQL database
PythonAnywhere deployment''',
                'categories': ['AI/ML', 'E-commerce'],
                'technologies': ['Python', 'Django', 'Scikit-learn', 'Pandas', 'NumPy', 'MySQL'],
                'github_url': 'https://github.com/AbdulSattar-07',
                'live_url': 'https://abdul007.pythonanywhere.com',
                'status': 'completed',
                'featured': True,
                'year': '2024–2025',
                'rating': 4.9,
                'order': 4
            },
            {
                'title': 'Diabetes Prediction ML Model',
                'slug': 'diabetes-prediction-ml',
                'description': 'Machine learning classification project for diabetes prediction using multiple ML algorithms and model evaluation techniques.',
                'full_description': '''Built a diabetes prediction machine learning model using the Pima Indians Diabetes Dataset. Trained and benchmarked Logistic Regression, Random Forest, SVM, and XGBoost models. Improved model performance using feature engineering, SMOTE oversampling, and GridSearchCV hyperparameter tuning.''',
                'features': '''Logistic Regression
Random Forest
Support Vector Machine
XGBoost
Feature engineering
SMOTE oversampling
GridSearchCV hyperparameter tuning
82% accuracy
AUC = 0.87
Confusion matrix
ROC-AUC curves
Precision-recall analysis''',
                'categories': ['AI/ML', 'Healthcare', 'Classification'],
                'technologies': ['Python', 'Scikit-learn', 'Pandas', 'Matplotlib', 'Jupyter Notebook', 'XGBoost', 'SMOTE'],
                'github_url': 'https://github.com/AbdulSattar-07',
                'live_url': '',
                'status': 'completed',
                'featured': False,
                'year': '2024',
                'rating': 4.7,
                'order': 5
            },
            {
                'title': 'Employee Management System',
                'slug': 'employee-management-system',
                'description': 'Complete Django-based HR management system with CRUD, RBAC, attendance, leave management, and payroll calculation.',
                'full_description': '''Built a complete employee management system using Django and MySQL. The system includes employee CRUD operations, role-based access control, attendance tracking, leave management, and payroll calculation. The database was designed using a normalized 3NF MySQL schema with 12 relational tables.''',
                'features': '''Employee CRUD system
Role-based access control
Attendance tracking
Leave management
Payroll calculation
Django backend
MySQL database
Bootstrap UI
3NF normalized database schema
12 relational tables''',
                'categories': ['Web Development', 'Django', 'HR System'],
                'technologies': ['Python', 'Django', 'MySQL', 'Bootstrap', 'HTML/CSS'],
                'github_url': 'https://github.com/AbdulSattar-07',
                'live_url': '',
                'status': 'completed',
                'featured': False,
                'year': '2024',
                'rating': 4.6,
                'order': 6
            }
        ]
        
        for project_data in projects_data:
            categories = project_data.pop('categories')
            technologies = project_data.pop('technologies')
            
            project, created = Project.objects.get_or_create(
                slug=project_data['slug'],
                defaults=project_data
            )
            
            # Add categories
            for cat_name in categories:
                try:
                    cat = Category.objects.get(name=cat_name)
                    project.categories.add(cat)
                except Category.DoesNotExist:
                    pass
            
            # Add technologies
            for tech_name in technologies:
                try:
                    tech = Technology.objects.get(name=tech_name)
                    project.technologies.add(tech)
                except Technology.DoesNotExist:
                    pass
        
        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(projects_data)} Projects'))

    def populate_achievements(self):
        """Populate Achievements"""
        achievements = [
            {
                'title': 'Production Deployment',
                'description': 'Built and deployed live enterprise ERP AI systems at Royal Soft serving real business operations.',
                'icon': 'fas fa-rocket',
                'date': date(2026, 3, 1),
                'category': 'Professional',
                'order': 1
            },
            {
                'title': '3.78 / 4.00 GPA',
                'description': 'Graduated in the top 10% of class while simultaneously building production AI systems.',
                'icon': 'fas fa-graduation-cap',
                'date': date(2025, 6, 1),
                'category': 'Academic',
                'order': 2
            },
            {
                'title': 'Multi-Agent Architect',
                'description': 'Designed and shipped scalable multi-agent LangChain systems across production projects at Royal Soft.',
                'icon': 'fas fa-project-diagram',
                'date': date(2026, 3, 1),
                'category': 'Technical',
                'order': 3
            },
            {
                'title': 'AI Code Generation System',
                'description': 'Built a RAG-based PHP ERP code generation system trained on 1,400+ company code files and achieved 70–90% code similarity with the real ERP codebase.',
                'icon': 'fas fa-code',
                'date': date(2026, 2, 1),
                'category': 'Innovation',
                'order': 4
            },
            {
                'title': 'Workflow Automation Impact',
                'description': 'Built an SDLC automation bot that reduced project kick-off time by 60%+ through AI-powered task planning and TMS API integration.',
                'icon': 'fas fa-cogs',
                'date': date(2026, 1, 1),
                'category': 'Impact',
                'order': 5
            }
        ]
        
        for achievement_data in achievements:
            Achievement.objects.get_or_create(
                title=achievement_data['title'],
                defaults=achievement_data
            )
        
        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(achievements)} Achievements'))

    def populate_certifications(self):
        """Populate Certifications"""
        certifications = [
            'Production AI Systems — Royal Soft enterprise deployment experience',
            'Multi-Agent GenAI Architecture — LangChain, LangGraph, RAG, ChromaDB',
            'Machine Learning Engineering — Scikit-learn, model evaluation, feature engineering',
            'Django REST API Development — ORM, authentication, MySQL integration',
            'Workflow Automation — n8n, OpenAI GPT pipeline, REST API integration'
        ]
        
        for idx, cert_title in enumerate(certifications, 1):
            Certification.objects.get_or_create(
                title=cert_title,
                defaults={'section': 'resume', 'order': idx}
            )
        
        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(certifications)} Certifications'))

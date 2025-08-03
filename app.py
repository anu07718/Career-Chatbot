# app.py - Main Flask Application
from flask import Flask, render_template, request, jsonify
import re
import json
from datetime import datetime
import random

app = Flask(__name__)

class CareerChatbot:
    def __init__(self):
        self.career_database = {
            'technology': {
                'keywords': ['tech', 'technology', 'programming', 'coding', 'software', 'computer', 'ai', 'machine learning', 'data', 'web development'],
                'careers': [
                    {
                        'title': 'Software Developer',
                        'description': 'Design, develop, and maintain software applications and systems using various programming languages.',
                        'skills': ['Python/Java/JavaScript', 'Problem Solving', 'Software Architecture', 'Database Management', 'Version Control (Git)'],
                        'salary_range': '$70,000 - $150,000+',
                        'growth_rate': 'High (22% growth expected)',
                        'education': 'Bachelor\'s in Computer Science or related field',
                        'roadmap': [
                            {'step': 1, 'title': 'Learn Programming Fundamentals', 'duration': '3-6 months', 'description': 'Master basic programming concepts, syntax, and logic'},
                            {'step': 2, 'title': 'Choose a Programming Language', 'duration': '2-4 months', 'description': 'Specialize in Python, Java, JavaScript, or C++'},
                            {'step': 3, 'title': 'Build Personal Projects', 'duration': '3-6 months', 'description': 'Create portfolio projects to demonstrate skills'},
                            {'step': 4, 'title': 'Learn Version Control', 'duration': '1 month', 'description': 'Master Git and GitHub for code management'},
                            {'step': 5, 'title': 'Data Structures & Algorithms', 'duration': '3-4 months', 'description': 'Study fundamental CS concepts for interviews'},
                            {'step': 6, 'title': 'Apply for Entry-Level Positions', 'duration': '1-3 months', 'description': 'Prepare resume, practice interviews, apply for jobs'},
                            {'step': 7, 'title': 'Gain Professional Experience', 'duration': '2-3 years', 'description': 'Work in entry-level developer roles'},
                            {'step': 8, 'title': 'Specialize in Domain', 'duration': '1-2 years', 'description': 'Focus on web, mobile, AI, or other specialization'},
                            {'step': 9, 'title': 'Senior Developer Role', 'duration': '2-4 years', 'description': 'Lead projects and mentor junior developers'},
                            {'step': 10, 'title': 'Technical Leadership', 'duration': 'Ongoing', 'description': 'Architect, team lead, or technical director roles'}
                        ]
                    },
                    {
                        'title': 'Data Scientist',
                        'description': 'Analyze complex data to extract insights and help organizations make data-driven decisions.',
                        'skills': ['Python/R', 'Statistics', 'Machine Learning', 'Data Visualization', 'SQL', 'Domain Knowledge'],
                        'salary_range': '$80,000 - $160,000+',
                        'growth_rate': 'Very High (35% growth expected)',
                        'education': 'Bachelor\'s in Statistics, Math, CS, or related field',
                        'roadmap': [
                            {'step': 1, 'title': 'Mathematics & Statistics Foundation', 'duration': '3-4 months', 'description': 'Linear algebra, calculus, probability, and statistics'},
                            {'step': 2, 'title': 'Learn Python/R Programming', 'duration': '2-3 months', 'description': 'Focus on data manipulation libraries (pandas, NumPy)'},
                            {'step': 3, 'title': 'Data Analysis & Visualization', 'duration': '2-3 months', 'description': 'Master matplotlib, seaborn, plotly, or ggplot2'},
                            {'step': 4, 'title': 'Machine Learning Fundamentals', 'duration': '4-6 months', 'description': 'Supervised and unsupervised learning algorithms'},
                            {'step': 5, 'title': 'Database & SQL Skills', 'duration': '1-2 months', 'description': 'Learn to extract and manipulate data from databases'},
                            {'step': 6, 'title': 'Build Portfolio Projects', 'duration': '3-4 months', 'description': 'Complete end-to-end data science projects'},
                            {'step': 7, 'title': 'Advanced ML & Deep Learning', 'duration': '4-6 months', 'description': 'Neural networks, TensorFlow, PyTorch'},
                            {'step': 8, 'title': 'Apply for Data Roles', 'duration': '2-4 months', 'description': 'Data analyst, junior data scientist positions'},
                            {'step': 9, 'title': 'Gain Industry Experience', 'duration': '2-3 years', 'description': 'Work on real business problems'},
                            {'step': 10, 'title': 'Senior Data Scientist', 'duration': 'Ongoing', 'description': 'Lead data initiatives and mentor teams'}
                        ]
                    },
                    {
                        'title': 'Cybersecurity Analyst',
                        'description': 'Protect organizations from cyber threats by monitoring, detecting, and responding to security incidents.',
                        'skills': ['Network Security', 'Ethical Hacking', 'Risk Assessment', 'Security Frameworks', 'Incident Response'],
                        'salary_range': '$75,000 - $140,000+',
                        'growth_rate': 'Very High (33% growth expected)',
                        'education': 'Bachelor\'s in Cybersecurity, IT, or related field',
                        'roadmap': [
                            {'step': 1, 'title': 'IT Fundamentals', 'duration': '2-3 months', 'description': 'Learn networking, operating systems, and basic IT concepts'},
                            {'step': 2, 'title': 'Cybersecurity Principles', 'duration': '3-4 months', 'description': 'Study CIA triad, threat landscape, and security frameworks'},
                            {'step': 3, 'title': 'CompTIA Security+ Certification', 'duration': '2-3 months', 'description': 'Get foundational cybersecurity certification'},
                            {'step': 4, 'title': 'Hands-on Security Tools', 'duration': '3-4 months', 'description': 'Learn SIEM, vulnerability scanners, and forensic tools'},
                            {'step': 5, 'title': 'Ethical Hacking Skills', 'duration': '4-6 months', 'description': 'Penetration testing and vulnerability assessment'},
                            {'step': 6, 'title': 'Build Home Lab', 'duration': '1-2 months', 'description': 'Create virtual environment for practice'},
                            {'step': 7, 'title': 'Entry-Level Security Role', 'duration': '3-6 months job search', 'description': 'SOC analyst or junior security analyst'},
                            {'step': 8, 'title': 'Advanced Certifications', 'duration': '6-12 months', 'description': 'CISSP, CEH, or GCIH certifications'},
                            {'step': 9, 'title': 'Specialize in Domain', 'duration': '1-2 years', 'description': 'Focus on incident response, pentesting, or compliance'},
                            {'step': 10, 'title': 'Senior Security Roles', 'duration': 'Ongoing', 'description': 'Security architect, CISO, or consultant positions'}
                        ]
                    }
                ]
            },
            'healthcare': {
                'keywords': ['health', 'healthcare', 'medical', 'medicine', 'nursing', 'doctor', 'therapy', 'helping people', 'patient care'],
                'careers': [
                    {
                        'title': 'Registered Nurse (RN)',
                        'description': 'Provide direct patient care, administer medications, and coordinate with healthcare teams.',
                        'skills': ['Patient Care', 'Medical Knowledge', 'Communication', 'Critical Thinking', 'Compassion'],
                        'salary_range': '$60,000 - $90,000+',
                        'growth_rate': 'High (15% growth expected)',
                        'education': 'Associate or Bachelor\'s degree in Nursing',
                        'roadmap': [
                            {'step': 1, 'title': 'Complete Prerequisites', 'duration': '1-2 years', 'description': 'High school diploma with strong science grades'},
                            {'step': 2, 'title': 'Nursing Program', 'duration': '2-4 years', 'description': 'ADN (2 years) or BSN (4 years) program'},
                            {'step': 3, 'title': 'Clinical Rotations', 'duration': 'Throughout program', 'description': 'Hands-on experience in various healthcare settings'},
                            {'step': 4, 'title': 'NCLEX-RN Exam', 'duration': '1-3 months prep', 'description': 'Pass national licensing examination'},
                            {'step': 5, 'title': 'Entry-Level RN Position', 'duration': '6 months - 1 year', 'description': 'Gain experience in preferred specialty area'},
                            {'step': 6, 'title': 'BSN Completion (if ADN)', 'duration': '1-2 years', 'description': 'Many employers prefer BSN-prepared nurses'},
                            {'step': 7, 'title': 'Specialty Certification', 'duration': '1-2 years experience + cert', 'description': 'ICU, ER, pediatrics, or other specialty'},
                            {'step': 8, 'title': 'Advanced Practice Consider', 'duration': '2-3 years experience', 'description': 'Nurse practitioner or nurse educator path'},
                            {'step': 9, 'title': 'Leadership Roles', 'duration': '5+ years experience', 'description': 'Charge nurse, nurse manager positions'},
                            {'step': 10, 'title': 'Advanced Nursing Roles', 'duration': 'MSN required', 'description': 'Nurse practitioner, clinical nurse specialist'}
                        ]
                    },
                    {
                        'title': 'Physical Therapist',
                        'description': 'Help patients recover from injuries, surgeries, and chronic conditions through therapeutic exercises.',
                        'skills': ['Anatomy & Physiology', 'Rehabilitation Techniques', 'Patient Assessment', 'Empathy', 'Manual Therapy'],
                        'salary_range': '$75,000 - $95,000+',
                        'growth_rate': 'Very High (28% growth expected)',
                        'education': 'Doctoral degree in Physical Therapy (DPT)',
                        'roadmap': [
                            {'step': 1, 'title': 'Bachelor\'s Degree', 'duration': '4 years', 'description': 'Complete prerequisites: biology, chemistry, physics, psychology'},
                            {'step': 2, 'title': 'Healthcare Experience', 'duration': '6 months - 1 year', 'description': 'Volunteer or work in healthcare settings'},
                            {'step': 3, 'title': 'DPT Program Application', 'duration': '1 year', 'description': 'Apply to accredited physical therapy programs'},
                            {'step': 4, 'title': 'DPT Program', 'duration': '3 years', 'description': 'Complete doctoral degree in physical therapy'},
                            {'step': 5, 'title': 'Clinical Internships', 'duration': 'Throughout DPT', 'description': 'Hands-on experience in various PT settings'},
                            {'step': 6, 'title': 'NPTE Exam', 'duration': '1-2 months prep', 'description': 'Pass National Physical Therapy Examination'},
                            {'step': 7, 'title': 'State Licensing', 'duration': '1-2 months', 'description': 'Obtain license to practice in your state'},
                            {'step': 8, 'title': 'Entry-Level PT Position', 'duration': '1-2 years', 'description': 'Gain experience in outpatient or hospital setting'},
                            {'step': 9, 'title': 'Specialization', 'duration': '1-3 years + cert', 'description': 'Orthopedics, sports, neurology, or pediatrics'},
                            {'step': 10, 'title': 'Advanced Practice', 'duration': '5+ years experience', 'description': 'Private practice, research, or teaching roles'}
                        ]
                    }
                ]
            },
            'business': {
                'keywords': ['business', 'finance', 'management', 'entrepreneur', 'marketing', 'sales', 'consulting', 'leadership'],
                'careers': [
                    {
                        'title': 'Business Analyst',
                        'description': 'Analyze business processes, identify improvement opportunities, and recommend solutions.',
                        'skills': ['Data Analysis', 'Process Improvement', 'Requirements Gathering', 'Communication', 'Problem Solving'],
                        'salary_range': '$60,000 - $100,000+',
                        'growth_rate': 'High (14% growth expected)',
                        'education': 'Bachelor\'s in Business, Economics, or related field',
                        'roadmap': [
                            {'step': 1, 'title': 'Business Fundamentals', 'duration': '3-6 months', 'description': 'Learn basic business processes and terminology'},
                            {'step': 2, 'title': 'Excel & Data Analysis', 'duration': '2-3 months', 'description': 'Master advanced Excel, basic SQL, and data visualization'},
                            {'step': 3, 'title': 'Process Modeling', 'duration': '2-3 months', 'description': 'Learn process mapping, flowcharts, and improvement methodologies'},
                            {'step': 4, 'title': 'Requirements Analysis', 'duration': '2-3 months', 'description': 'Study requirements gathering and documentation techniques'},
                            {'step': 5, 'title': 'Build Portfolio', 'duration': '3-4 months', 'description': 'Create case studies and analysis examples'},
                            {'step': 6, 'title': 'Entry-Level BA Role', 'duration': '3-6 months job search', 'description': 'Junior business analyst or associate positions'},
                            {'step': 7, 'title': 'Industry Experience', 'duration': '2-3 years', 'description': 'Gain experience in specific industry or domain'},
                            {'step': 8, 'title': 'BA Certifications', 'duration': '6-12 months', 'description': 'CBAP, CCBA, or other business analysis certifications'},
                            {'step': 9, 'title': 'Senior BA Role', 'duration': '3-5 years experience', 'description': 'Lead analysis projects and mentor junior analysts'},
                            {'step': 10, 'title': 'Consulting or Management', 'duration': '5+ years experience', 'description': 'Business consultant or analysis manager roles'}
                        ]
                    },
                    {
                        'title': 'Digital Marketing Manager',
                        'description': 'Develop and execute digital marketing strategies across various online platforms.',
                        'skills': ['Digital Strategy', 'Content Creation', 'SEO/SEM', 'Social Media', 'Analytics', 'Campaign Management'],
                        'salary_range': '$55,000 - $95,000+',
                        'growth_rate': 'High (19% growth expected)',
                        'education': 'Bachelor\'s in Marketing, Communications, or related field',
                        'roadmap': [
                            {'step': 1, 'title': 'Marketing Fundamentals', 'duration': '2-3 months', 'description': 'Learn basic marketing principles and consumer behavior'},
                            {'step': 2, 'title': 'Digital Platforms', 'duration': '2-3 months', 'description': 'Master social media platforms and digital advertising'},
                            {'step': 3, 'title': 'Content Creation', 'duration': '3-4 months', 'description': 'Develop copywriting, design, and video creation skills'},
                            {'step': 4, 'title': 'SEO & Analytics', 'duration': '2-3 months', 'description': 'Learn search engine optimization and Google Analytics'},
                            {'step': 5, 'title': 'Paid Advertising', 'duration': '2-3 months', 'description': 'Google Ads, Facebook Ads, and other PPC platforms'},
                            {'step': 6, 'title': 'Build Portfolio', 'duration': '3-4 months', 'description': 'Create campaigns for personal brand or mock clients'},
                            {'step': 7, 'title': 'Entry-Level Position', 'duration': '2-4 months job search', 'description': 'Digital marketing coordinator or specialist role'},
                            {'step': 8, 'title': 'Campaign Management', 'duration': '1-2 years', 'description': 'Run and optimize digital marketing campaigns'},
                            {'step': 9, 'title': 'Advanced Certifications', 'duration': '6-12 months', 'description': 'Google Ads, HubSpot, Facebook Blueprint certifications'},
                            {'step': 10, 'title': 'Marketing Manager', 'duration': '3-5 years experience', 'description': 'Lead digital marketing strategy and team'}
                        ]
                    }
                ]
            },
            'creative': {
                'keywords': ['creative', 'art', 'design', 'visual', 'graphic', 'ui', 'ux', 'web design', 'artistic', 'creativity'],
                'careers': [
                    {
                        'title': 'UX/UI Designer',
                        'description': 'Design user-friendly interfaces and experiences for websites, apps, and digital products.',
                        'skills': ['Design Software', 'User Research', 'Prototyping', 'Visual Design', 'Usability Testing', 'Design Thinking'],
                        'salary_range': '$65,000 - $120,000+',
                        'growth_rate': 'High (13% growth expected)',
                        'education': 'Bachelor\'s in Design, Psychology, or related field',
                        'roadmap': [
                            {'step': 1, 'title': 'Design Fundamentals', 'duration': '2-3 months', 'description': 'Learn color theory, typography, and visual hierarchy'},
                            {'step': 2, 'title': 'Design Software', 'duration': '3-4 months', 'description': 'Master Figma, Adobe Creative Suite, and Sketch'},
                            {'step': 3, 'title': 'User Research Methods', 'duration': '2-3 months', 'description': 'Learn user interviews, surveys, and usability testing'},
                            {'step': 4, 'title': 'Wireframing & Prototyping', 'duration': '2-3 months', 'description': 'Create low and high-fidelity prototypes'},
                            {'step': 5, 'title': 'Portfolio Development', 'duration': '4-6 months', 'description': 'Build 3-5 comprehensive UX case studies'},
                            {'step': 6, 'title': 'Web Technologies Basics', 'duration': '2-3 months', 'description': 'Learn HTML, CSS basics for better collaboration'},
                            {'step': 7, 'title': 'Entry-Level UX Role', 'duration': '3-6 months job search', 'description': 'Junior UX/UI designer or design intern'},
                            {'step': 8, 'title': 'Real Project Experience', 'duration': '1-2 years', 'description': 'Work on actual products and user problems'},
                            {'step': 9, 'title': 'Specialization', 'duration': '2-3 years', 'description': 'Focus on mobile, web, or specific industry'},
                            {'step': 10, 'title': 'Senior Designer', 'duration': '3-5 years experience', 'description': 'Lead design projects and mentor junior designers'}
                        ]
                    }
                ]
            },
            'education': {
                'keywords': ['education', 'teaching', 'training', 'instructor', 'academic', 'learning', 'curriculum'],
                'careers': [
                    {
                        'title': 'Elementary School Teacher',
                        'description': 'Teach and nurture young students in foundational subjects and social skills.',
                        'skills': ['Curriculum Development', 'Classroom Management', 'Child Psychology', 'Patience', 'Communication'],
                        'salary_range': '$45,000 - $70,000+',
                        'growth_rate': 'Moderate (8% growth expected)',
                        'education': 'Bachelor\'s in Education or subject area + teaching credential',
                        'roadmap': [
                            {'step': 1, 'title': 'Bachelor\'s Degree', 'duration': '4 years', 'description': 'Education degree or subject area with education minor'},
                            {'step': 2, 'title': 'Teacher Preparation Program', 'duration': '1 year', 'description': 'Complete state-approved teacher preparation program'},
                            {'step': 3, 'title': 'Student Teaching', 'duration': '1 semester', 'description': 'Supervised classroom experience with mentor teacher'},
                            {'step': 4, 'title': 'Teaching Credential', 'duration': '2-6 months', 'description': 'Pass state exams and obtain teaching license'},
                            {'step': 5, 'title': 'Job Search & Interviews', 'duration': '3-6 months', 'description': 'Apply for teaching positions in school districts'},
                            {'step': 6, 'title': 'First Year Teaching', 'duration': '1 year', 'description': 'Complete probationary first year with support'},
                            {'step': 7, 'title': 'Continuing Education', 'duration': 'Ongoing', 'description': 'Meet professional development requirements'},
                            {'step': 8, 'title': 'Master\'s Degree', 'duration': '2-3 years part-time', 'description': 'Often required for permanent certification'},
                            {'step': 9, 'title': 'Specialization/Leadership', 'duration': '5+ years experience', 'description': 'Department head, curriculum specialist, or mentor teacher'},
                            {'step': 10, 'title': 'Administration Path', 'duration': 'Additional degree + experience', 'description': 'Principal, assistant principal, or district roles'}
                        ]
                    }
                ]
            }
        }
        
        self.conversation_history = []
        
    def preprocess_message(self, message):
        """Clean and preprocess user message"""
        return message.lower().strip()
    
    def extract_interests(self, message):
        """Extract interests and keywords from user message"""
        processed_message = self.preprocess_message(message)
        found_categories = []
        
        for category, data in self.career_database.items():
            for keyword in data['keywords']:
                if keyword in processed_message:
                    if category not in found_categories:
                        found_categories.append(category)
                    break
                    
        return found_categories
    
    def analyze_user_intent(self, message):
        """Analyze user intent from message"""
        processed_message = self.preprocess_message(message)
        
        intents = {
            'career_search': ['career', 'job', 'profession', 'work', 'occupation'],
            'roadmap_request': ['roadmap', 'path', 'steps', 'how to become', 'guide', 'plan'],
            'salary_inquiry': ['salary', 'pay', 'money', 'earn', 'income', 'wage'],
            'education_inquiry': ['degree', 'education', 'study', 'college', 'university'],
            'skills_inquiry': ['skills', 'abilities', 'requirements', 'qualifications']
        }
        
        detected_intents = []
        for intent, keywords in intents.items():
            if any(keyword in processed_message for keyword in keywords):
                detected_intents.append(intent)
                
        return detected_intents if detected_intents else ['career_search']
    
    def generate_career_suggestions(self, categories):
        """Generate career suggestions based on categories"""
        suggestions = []
        for category in categories:
            if category in self.career_database:
                suggestions.extend(self.career_database[category]['careers'])
        return suggestions
    
    def format_career_response(self, careers, intents):
        """Format career information based on user intents"""
        if not careers:
            return self.get_general_help_response()
            
        response = {
            'message': '',
            'careers': [],
            'suggestions': []
        }
        
        # Personalized greeting based on number of careers found
        if len(careers) == 1:
            response['message'] = "Perfect! I found an excellent career match for your interests:"
        else:
            response['message'] = f"Great! I found {len(careers)} career options that align with your interests:"
        
        for career in careers:
            career_info = {
                'title': career['title'],
                'description': career['description'],
                'skills': career['skills'],
                'salary_range': career['salary_range'],
                'growth_rate': career['growth_rate'],
                'education': career['education'],
                'roadmap': career['roadmap']
            }
            
            # Add specific information based on user intents
            if 'salary_inquiry' in intents:
                career_info['highlight'] = 'salary'
            elif 'education_inquiry' in intents:
                career_info['highlight'] = 'education'
            elif 'skills_inquiry' in intents:
                career_info['highlight'] = 'skills'
            elif 'roadmap_request' in intents:
                career_info['highlight'] = 'roadmap'
                
            response['careers'].append(career_info)
        
        # Add follow-up suggestions
        response['suggestions'] = [
            "Would you like to see a detailed roadmap for any of these careers?",
            "Do you want to know more about the required skills?",
            "Are you curious about salary progression in these fields?",
            "Would you like career comparisons or alternatives?"
        ]
        
        return response
    
    def get_general_help_response(self):
        """Generate response when no specific careers are found"""
        return {
            'message': "I'd love to help you explore career options! I can assist you with careers in:",
            'careers': [],
            'categories': [
                {'name': 'Technology', 'description': 'Software development, data science, cybersecurity'},
                {'name': 'Healthcare', 'description': 'Nursing, physical therapy, medical fields'},
                {'name': 'Business', 'description': 'Analysis, marketing, management, consulting'},
                {'name': 'Creative', 'description': 'UX/UI design, graphic design, digital arts'},
                {'name': 'Education', 'description': 'Teaching, training, curriculum development'}
            ],
            'suggestions': [
                "Tell me about your interests or hobbies",
                "What subjects do you enjoy most?",
                "Do you prefer working with people, data, or creative projects?",
                "Are you interested in any specific industry?"
            ]
        }
    
    def generate_roadmap_response(self, career_title):
        """Generate detailed roadmap response for a specific career"""
        for category_data in self.career_database.values():
            for career in category_data['careers']:
                if career['title'].lower() == career_title.lower():
                    return {
                        'message': f"Here's your personalized roadmap to become a {career['title']}:",
                        'career': career,
                        'roadmap': career['roadmap'],
                        'tips': [
                            "Focus on building a strong portfolio throughout your journey",
                            "Network with professionals in your target field",
                            "Consider finding a mentor in the industry",
                            "Stay updated with industry trends and technologies"
                        ]
                    }
        return None
    
    def process_message(self, message):
        """Main method to process user messages and generate responses"""
        # Add to conversation history
        self.conversation_history.append({
            'timestamp': datetime.now(),
            'user_message': message,
            'type': 'user'
        })
        
        # Extract interests and analyze intent
        categories = self.extract_interests(message)
        intents = self.analyze_user_intent(message)
        
        # Check if user is asking for a specific career roadmap
        processed_msg = self.preprocess_message(message)
        if 'roadmap' in processed_msg or 'how to become' in processed_msg:
            # Try to extract career title from message
            for category_data in self.career_database.values():
                for career in category_data['careers']:
                    if career['title'].lower() in processed_msg:
                        roadmap_response = self.generate_roadmap_response(career['title'])
                        if roadmap_response:
                            self.conversation_history.append({
                                'timestamp': datetime.now(),
                                'bot_response': roadmap_response,
                                'type': 'bot'
                            })
                            return roadmap_response
        
        # Generate career suggestions
        careers = self.generate_career_suggestions(categories)
        
        # Limit to top 3 careers to avoid overwhelming the user
        if len(careers) > 3:
            careers = careers[:3]
            
        response = self.format_career_response(careers, intents)
        
        # Add to conversation history
        self.conversation_history.append({
            'timestamp': datetime.now(),
            'bot_response': response,
            'type': 'bot'
        })
        
        return response

# Initialize chatbot
chatbot = CareerChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Process message through chatbot
        response = chatbot.process_message(user_message)
        
        return jsonify({
            'success': True,
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/roadmap/<career_title>')
def get_roadmap(career_title):
    try:
        roadmap_response = chatbot.generate_roadmap_response(career_title)
        if roadmap_response:
            return jsonify({
                'success': True,
                'roadmap': roadmap_response
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Career not found'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/history')
def get_conversation_history():
    try:
        return jsonify({
            'success': True,
            'history': chatbot.conversation_history[-10:]  # Last 10 messages
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
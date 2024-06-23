from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from .models import SEO_tag, Type_words, Description, Fact, Service, Skill, Testimonial
from Contact_And_Feedback.models import ContactAndFeedBacks
from PortFolio.models import Portfolio, PortfolioDetails
from DPO.settings import EMAIL_HOST_USER

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            # Create a new entry in ContactAndFeedBacks model
            contact_entry = ContactAndFeedBacks.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            # Send email to user
            mes_e = ''
            with open('Home/email/email.html', 'r') as file:
                mes_e = file.read()  # Read HTML content from file
            sub = "Thanks For Contacting Us"
            to = [email]
            html_email = EmailMultiAlternatives(sub, mes_e, EMAIL_HOST_USER, to)
            html_email.content_subtype = 'html'
            html_email.send()

            # Get all admin or staff emails
            admin_emails = list(User.objects.filter(is_staff=True).values_list('email', flat=True))

              # Render the email content from template
            email_content = render_to_string('Home/email/admin_email.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            })

            # Send email to admin/staff members
            mes_admin = ''
            with open('Home/email/admin_email.html', 'r') as file:
                mes_admin = file.read()  # Read HTML content from file
            admin_sub = "New Feedback is Appear in DPO"
            mes_admin = email_content
            html_email_admin = EmailMultiAlternatives(admin_sub, mes_admin, EMAIL_HOST_USER, admin_emails)
            html_email_admin.content_subtype = 'html'
            html_email_admin.send()

            # Update status and notify user
            contact_entry.email_send_status = True
            contact_entry.save()
            messages.success(request, "Your Message Has Been Sent!")

        except Exception as e:
            messages.warning(request, f"Something went wrong - please try again! Error: {str(e)}")

    # Fetching data for rendering the homepage
    tag = SEO_tag.objects.first()
    word = Type_words.objects.all()
    cate = Portfolio.objects.values('portfolio_category').distinct()
    portfolios = Portfolio.objects.all()
    testimonial = Testimonial.objects.all()
    skill = Skill.objects.all()
    service = Service.objects.all()
    fact = Fact.objects.all()
    sections = Description.objects.all()
    content = {section.title: section for section in sections}

    data = {
        'word': word,
        'tag': tag,
        'portfolios': portfolios,
        'cate': cate,
        'test': testimonial,
        'skill': skill,
        'service': service,
        'fact': fact,
        'content': content,
    }

    return render(request, 'index.html', data)

def portfoliodetails(request, portfolio_name):
    portfolio = get_object_or_404(Portfolio, portfolio_url=portfolio_name)
    details = PortfolioDetails.objects.get(portfolio_name=portfolio)
    data = {
        'data': details,
        'portfolio': portfolio,
    }
    return render(request, "portfolio-details.html", data)

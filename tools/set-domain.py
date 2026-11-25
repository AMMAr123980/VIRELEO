#!/usr/bin/env python3
"""
Advanced SEO, AEO & GEO Automation for VIRELEO
Run with:
    python tools/set-domain.py https://vireleo.me

Features:
- Absolute Google Search Favicon priority tags (48x48 primary, 192x192, 512x512, shortcut icon)
- AEO / GEO Entity Grounding (Wikipedia / Wikidata entity definitions in knowsAbout)
- SpeakableSpecification for AI engines and voice answer queries
- Standardized Open Graph & Twitter Card metadata per page
- Rich Schema: Organization, ProfessionalService, WebSite, WebPage, BreadcrumbList, OfferCatalog, Services, ItemList
- Dynamic Google-compliant XML Sitemap with priorities and changefreq
- Explicit Googlebot & Googlebot-Favicon permissions in robots.txt
"""
import sys, re, json, datetime, pathlib, html

if len(sys.argv) != 2 or not re.match(r'^https://[a-z0-9.-]+\.[a-z]{2,}(:\d+)?$', sys.argv[1].rstrip('/'), re.I):
    sys.exit('Usage: python tools/set-domain.py https://vireleo.me   (must start with https://, no path)')

SITE = sys.argv[1].rstrip('/')
ROOT = pathlib.Path(__file__).resolve().parent.parent
TODAY = datetime.date.today().isoformat()

PAGES = [  # file, path, schema type, breadcrumb name, priority, changefreq
    ('index.html', '/', 'WebPage', None, '1.0', 'weekly'),
    ('website-development.html', '/website-development.html', 'WebPage', 'Website Development', '0.9', 'monthly'),
    ('app-development.html', '/app-development.html', 'WebPage', 'App Development', '0.9', 'monthly'),
    ('ai-automation.html', '/ai-automation.html', 'WebPage', 'AI Automation', '0.9', 'monthly'),
    ('ai-chatbots.html', '/ai-chatbots.html', 'WebPage', 'AI Chatbots', '0.9', 'monthly'),
    ('work.html', '/work.html', 'CollectionPage', 'Work', '0.8', 'weekly'),
    ('capabilities.html', '/capabilities.html', 'CollectionPage', 'Capabilities', '0.8', 'monthly'),
    ('about.html', '/about.html', 'AboutPage', 'About', '0.7', 'monthly'),
    ('blog.html', '/blog.html', 'CollectionPage', 'Blog', '0.85', 'weekly'),
    ('blog-cost-to-build-saas-mvp.html', '/blog-cost-to-build-saas-mvp.html', 'BlogPosting', 'SaaS MVP Cost', '0.85', 'monthly'),
    ('blog-cost-to-build-an-mvp.html', '/blog-cost-to-build-an-mvp.html', 'BlogPosting', 'MVP Development Cost', '0.85', 'monthly'),
    ('blog-custom-code-vs-wordpress.html', '/blog-custom-code-vs-wordpress.html', 'BlogPosting', 'Custom Code vs WordPress', '0.85', 'monthly'),
    ('blog-whatsapp-instagram-ai-chatbot-guide.html', '/blog-whatsapp-instagram-ai-chatbot-guide.html', 'BlogPosting', 'WhatsApp & Instagram AI Bots', '0.85', 'monthly'),
    ('blog-ai-workflow-automation-guide.html', '/blog-ai-workflow-automation-guide.html', 'BlogPosting', 'AI Workflow Automation', '0.85', 'monthly'),
    ('contact.html', '/contact.html', 'ContactPage', 'Contact', '0.8', 'monthly'),
    ('privacy-policy.html', '/privacy-policy.html', 'WebPage', 'Privacy Policy', '0.5', 'yearly'),
]

SERVICES = [
    ('Website development', 'Custom-coded business websites, e-commerce, landing pages and web applications.', f'{SITE}/website-development.html'),
    ('Mobile app development', 'Mobile and web apps shaped around real workflows, users and outcomes.', f'{SITE}/app-development.html'),
    ('AI workflow automation', 'Connected, AI-assisted workflows that remove repetitive business tasks.', f'{SITE}/ai-automation.html'),
    ('AI chatbots and messaging automation', 'AI chatbots for websites, WhatsApp and Instagram direct messages.', f'{SITE}/ai-chatbots.html'),
]

js_path = ROOT / 'js' / 'script.js'
projects = []
if js_path.exists():
    js = js_path.read_text(encoding='utf-8')
    for m in re.finditer(r'\{\s*id:\s*"([^"]+)",\s*cat:\s*"([^"]+)",\s*title:\s*"([^"]+)",\s*desc:\s*"([^"]+)"(?:,\s*url:\s*"([^"]+)")?', js):
        projects.append(dict(id=m.group(1), title=m.group(3), desc=m.group(4), url=m.group(5)))

org_id = SITE + '/#organization'
site_id = SITE + '/#website'

org = {
    "@type": "Organization",
    "@id": org_id,
    "name": "VIRELEO",
    "alternateName": "VIRELEO Studio",
    "url": SITE + '/',
    "logo": {
        "@type": "ImageObject",
        "@id": SITE + '/#logo',
        "url": SITE + '/icon-512.png',
        "width": 512,
        "height": 512,
        "caption": "VIRELEO Logo"
    },
    "image": {
        "@type": "ImageObject",
        "url": SITE + '/images/og-image.jpg'
    },
    "description": "A digital engineering studio building custom-coded websites, applications, AI automation and chatbot integrations.",
    "founder": {
        "@type": "Person",
        "name": "Ammar Hassan Malik",
        "jobTitle": "Founder & Lead Engineer"
    },
    "contactPoint": {
        "@type": "ContactPoint",
        "email": "fitduo07@gmail.com",
        "telephone": "+92 321 5772078"
    },
    "areaServed": "Worldwide",
    "sameAs": [
        "https://www.instagram.com/vireleo.me/",
        "https://www.linkedin.com/in/vireleo-806625322/"
    ],
    "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "VIRELEO Services",
        "itemListElement": [
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "Website Development",
                    "url": f"{SITE}/website-development.html",
                    "provider": {"@id": org_id}
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "App Development",
                    "url": f"{SITE}/app-development.html",
                    "provider": {"@id": org_id}
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "AI Automation",
                    "url": f"{SITE}/ai-automation.html",
                    "provider": {"@id": org_id}
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "AI Chatbot Development",
                    "url": f"{SITE}/ai-chatbots.html",
                    "provider": {"@id": org_id}
                }
            }
        ]
    }
}

website = {
    "@type": "WebSite",
    "@id": site_id,
    "url": SITE + '/',
    "name": "VIRELEO",
    "publisher": {"@id": org_id},
    "inLanguage": "en"
}

def build_block(file, path, ptype, crumb, title, desc):
    url = SITE + path
    if file == 'index.html':
        graph = [
            org,
            website,
            {
                "@type": ["WebPage", "FAQPage"],
                "@id": f"{SITE}/#webpage",
                "url": f"{SITE}/",
                "name": "VIRELEO — Custom Web Development & AI Automation Agency",
                "description": "Global custom web development company and AI automation agency engineering custom web apps, mobile apps and SaaS platforms for growing businesses worldwide.",
                "isPartOf": {"@id": site_id},
                "about": {"@id": org_id},
                "publisher": {"@id": org_id},
                "primaryImageOfPage": {
                    "@type": "ImageObject",
                    "url": f"{SITE}/images/og-image.jpg"
                },
                "inLanguage": "en",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "How do I hire VIRELEO for custom web development and web app engineering?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "To hire VIRELEO for custom website or web application development, share your project requirements through the Contact page. VIRELEO reviews your technical specifications, architecture and timeline to deliver custom-coded software built from scratch without page builders or WordPress plugins."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "What services does an AI automation agency provide for businesses?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "VIRELEO builds autonomous business workflows, CRM integrations, API data pipelines, automated lead routing and document processing systems that eliminate repetitive manual tasks and accelerate operations."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Can you build custom AI chatbots for WhatsApp and Instagram DM automation?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Yes. VIRELEO develops custom AI chatbots integrated with official Meta APIs for WhatsApp and Instagram. The bots can provide customer support, capture and qualify leads, answer product questions and sync user data into a CRM."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "How much does custom web development or SaaS MVP engineering cost?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Custom software development and SaaS MVP engineering costs depend on feature scope, technical complexity, database design and third-party integrations. VIRELEO provides fixed-scope proposals, phased milestone delivery and complete source-code ownership."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Why choose custom-coded web applications over WordPress or Webflow?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Custom-coded applications provide loading-speed, security and architectural flexibility benefits without relying on third-party page-builder plugins, allowing the application to be tailored to specific business logic and scaling needs."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "How long does it take to develop a custom website, mobile app or AI solution?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Most standard business websites and AI chatbots launch within 1 to 2 weeks. Comprehensive full-stack web applications and SaaS MVPs typically require 3 to 6 weeks, with milestone demonstrations and codebase handover."
                        }
                    }
                ]
            }
        ]
    elif file == 'about.html':
        graph = [
            {
                "@type": "AboutPage",
                "@id": f"{SITE}/about.html#webpage",
                "url": f"{SITE}/about.html",
                "name": "About VIRELEO | Modern Digital Engineering Studio",
                "description": "Learn about VIRELEO, an AI-native digital engineering studio building custom-coded websites, applications, AI automation, and chatbot integrations.",
                "isPartOf": {"@id": site_id},
                "about": {"@id": org_id},
                "mainEntity": {"@id": org_id},
                "primaryImageOfPage": {"@id": f"{SITE}/about.html#primaryimage"},
                "breadcrumb": {"@id": f"{SITE}/about.html#breadcrumb"},
                "inLanguage": "en"
            },
            {
                "@type": "ImageObject",
                "@id": f"{SITE}/about.html#primaryimage",
                "url": f"{SITE}/images/og-image.jpg",
                "contentUrl": f"{SITE}/images/og-image.jpg"
            },
            {
                "@type": "Organization",
                "@id": org_id,
                "name": "VIRELEO",
                "alternateName": "VIRELEO Studio",
                "url": f"{SITE}/",
                "description": "A digital engineering studio building custom-coded websites, applications, AI automation and chatbot integrations.",
                "logo": {
                    "@type": "ImageObject",
                    "@id": f"{SITE}/#logo",
                    "url": f"{SITE}/icon-512.png",
                    "contentUrl": f"{SITE}/icon-512.png",
                    "width": 512,
                    "height": 512,
                    "caption": "VIRELEO Logo"
                },
                "image": {"@id": f"{SITE}/about.html#primaryimage"},
                "founder": {
                    "@type": "Person",
                    "name": "Ammar Hassan Malik"
                },
                "contactPoint": {
                    "@type": "ContactPoint",
                    "telephone": "+92 321 5772078",
                    "email": "fitduo07@gmail.com",
                    "contactType": "customer service"
                },
                "sameAs": [
                    "https://www.instagram.com/vireleo.me/",
                    "https://www.linkedin.com/in/vireleo-806625322/"
                ]
            },
            website,
            {
                "@type": "BreadcrumbList",
                "@id": f"{SITE}/about.html#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                    {"@type": "ListItem", "position": 2, "name": "About", "item": f"{SITE}/about.html"}
                ]
            },
            {
                "@type": "FAQPage",
                "@id": f"{SITE}/about.html#faq",
                "url": f"{SITE}/about.html#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "What is VIRELEO?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "VIRELEO is an AI-native digital engineering studio founded by Ammar Hassan Malik. We specialize in custom-coded website development, scalable web applications, SaaS MVPs, AI workflow automation, and intelligent WhatsApp chatbots."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Who does VIRELEO work with?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "We partner with early-stage startups, SaaS founders, and growing enterprises worldwide looking for high-performance software engineering without bloated page builders, agency layers, or recurring platform licenses."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "How does VIRELEO engineer digital products?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Every project follows a structured 4-phase agile engineering process: Discovery and Architecture (Week 1), UI and Core Feature Engineering (Weeks 2-3), API and Payment Integrations (Week 4), and Quality Assurance Handover with 100% source code ownership."
                        }
                    }
                ]
            }
        ]
    elif file == 'app-development.html':
        graph = [
            {
                "@type": "Service",
                "@id": f"{SITE}/app-development.html#service",
                "name": "App Development",
                "serviceType": "Custom web and mobile app development",
                "url": f"{SITE}/app-development.html",
                "description": "Custom app development for business dashboards, customer portals, internal workflow tools, mobile app experiences, prototypes, MVPs and API integrations.",
                "provider": {"@id": org_id},
                "hasOfferCatalog": {
                    "@type": "OfferCatalog",
                    "name": "App Development Services",
                    "itemListElement": [
                        {
                            "@type": "Offer",
                            "itemOffered": {
                                "@type": "Service",
                                "name": "Business dashboards and customer portals",
                                "description": "Focused applications that give teams and customers access to the information and actions they need."
                            }
                        },
                        {
                            "@type": "Offer",
                            "itemOffered": {
                                "@type": "Service",
                                "name": "Custom internal tools and workflow apps",
                                "description": "Interfaces that digitise specific operational steps and are shaped around real users."
                            }
                        },
                        {
                            "@type": "Offer",
                            "itemOffered": {
                                "@type": "Service",
                                "name": "Mobile app experiences and prototypes",
                                "description": "Mobile experiences and prototypes for validating product ideas and key user journeys."
                            }
                        },
                        {
                            "@type": "Offer",
                            "itemOffered": {
                                "@type": "Service",
                                "name": "MVPs, API integrations and third-party services",
                                "description": "MVP development and system integrations where reliable APIs and suitable permissions are available."
                            }
                        }
                    ]
                }
            },
            org,
            website,
            {
                "@type": "WebPage",
                "@id": f"{SITE}/app-development.html#webpage",
                "url": f"{SITE}/app-development.html",
                "name": "Custom Web & Mobile App Development — MVP Development Agency | VIRELEO",
                "description": "App development services for dashboards, portals, internal tools, mobile experiences, prototypes, MVPs and API integrations.",
                "isPartOf": {"@id": site_id},
                "about": {"@id": f"{SITE}/app-development.html#service"},
                "mainEntity": {"@id": f"{SITE}/app-development.html#service"},
                "breadcrumb": {"@id": f"{SITE}/app-development.html#breadcrumb"}
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{SITE}/app-development.html#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                    {"@type": "ListItem", "position": 2, "name": "App Development", "item": f"{SITE}/app-development.html"}
                ]
            }
        ]
    elif file == 'blog.html':
        graph = [
            org,
            website,
            {
                "@type": "CollectionPage",
                "@id": f"{SITE}/blog.html#webpage",
                "url": f"{SITE}/blog.html",
                "name": "Engineering Insights & Guides | VIRELEO Digital Studio",
                "description": "Detailed, research-backed guides covering development costs, tech stack selection, and AI workflow integration.",
                "isPartOf": {"@id": site_id},
                "about": {"@id": org_id},
                "publisher": {"@id": org_id},
                "breadcrumb": {"@id": f"{SITE}/blog.html#breadcrumb"},
                "mainEntity": {"@id": f"{SITE}/blog.html#itemlist"}
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{SITE}/blog.html#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                    {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog.html"}
                ]
            },
            {
                "@type": "ItemList",
                "@id": f"{SITE}/blog.html#itemlist",
                "name": "Featured Playbooks",
                "numberOfItems": 5,
                "itemListOrder": "https://schema.org/ItemListOrderAscending",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "SaaS MVP Development Cost in 2026: Pricing, Features & Budget",
                        "url": f"{SITE}/blog-cost-to-build-saas-mvp.html"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "MVP Development Cost in 2026: How Much Does an MVP Cost?",
                        "url": f"{SITE}/blog-cost-to-build-an-mvp.html"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": "Custom Code vs WordPress: Speed, Security & Scalability Comparison for Business",
                        "url": f"{SITE}/blog-custom-code-vs-wordpress.html"
                    },
                    {
                        "@type": "ListItem",
                        "position": 4,
                        "name": "How to Automate WhatsApp & Instagram DMs with Custom AI Chatbots (Meta Cloud API)",
                        "url": f"{SITE}/blog-whatsapp-instagram-ai-chatbot-guide.html"
                    },
                    {
                        "@type": "ListItem",
                        "position": 5,
                        "name": "AI Workflow Automation: How Small Businesses Save 20+ Hours Every Week",
                        "url": f"{SITE}/blog-ai-workflow-automation-guide.html"
                    }
                ]
            }
        ]
    elif file == 'capabilities.html':
        graph = [
            org,
            website,
            {
                "@type": "WebPage",
                "@id": f"{SITE}/capabilities.html#webpage",
                "url": f"{SITE}/capabilities.html",
                "name": "Engineering Capabilities & Technical Stack | VIRELEO",
                "description": "VIRELEO's core capabilities include website development, applications and software, AI automation, and AI chatbots.",
                "isPartOf": {"@id": site_id},
                "about": {"@id": org_id},
                "mainEntity": {"@id": f"{SITE}/capabilities.html#capabilities"},
                "inLanguage": "en"
            },
            {
                "@type": "ItemList",
                "@id": f"{SITE}/capabilities.html#capabilities",
                "name": "VIRELEO Core Capabilities",
                "numberOfItems": 4,
                "itemListOrder": "https://schema.org/ItemListOrderAscending",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "item": {
                            "@type": "Service",
                            "@id": f"{SITE}/website-development.html#service",
                            "name": "Website development",
                            "serviceType": "Website development",
                            "description": "Fast, responsive websites with clear messaging, accessible layouts, thoughtful interactions and search-friendly foundations.",
                            "url": f"{SITE}/website-development.html",
                            "provider": {"@id": org_id}
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "item": {
                            "@type": "Service",
                            "@id": f"{SITE}/app-development.html#service",
                            "name": "Applications & software",
                            "serviceType": "Application and software development",
                            "description": "Useful web applications shaped around the workflows, users and outcomes a business needs.",
                            "url": f"{SITE}/app-development.html",
                            "provider": {"@id": org_id}
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "item": {
                            "@type": "Service",
                            "@id": f"{SITE}/ai-automation.html#service",
                            "name": "AI automation",
                            "serviceType": "AI workflow automation",
                            "description": "Connections between routine tasks and business tools that reduce manual work while keeping people in control.",
                            "url": f"{SITE}/ai-automation.html",
                            "provider": {"@id": org_id}
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 4,
                        "item": {
                            "@type": "Service",
                            "@id": f"{SITE}/ai-chatbots.html#service",
                            "name": "AI chatbots",
                            "serviceType": "AI chatbot development",
                            "description": "Conversational experiences for answering common questions and supporting customer enquiries.",
                            "url": f"{SITE}/ai-chatbots.html",
                            "provider": {"@id": org_id}
                        }
                    }
                ]
            }
        ]
    elif file == 'contact.html':
        graph = [
            {
                "@type": "ContactPage",
                "@id": f"{SITE}/contact.html#webpage",
                "url": f"{SITE}/contact.html",
                "name": "Contact VIRELEO | Start Your Web, App or AI Project",
                "description": "Contact VIRELEO about custom website development, mobile app development, AI automation, and chatbot projects.",
                "isPartOf": {"@id": site_id},
                "about": {"@id": org_id},
                "breadcrumb": {"@id": f"{SITE}/contact.html#breadcrumb"},
                "hasPart": {"@id": f"{SITE}/contact.html#faq"}
            },
            org,
            website,
            {
                "@type": "BreadcrumbList",
                "@id": f"{SITE}/contact.html#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                    {"@type": "ListItem", "position": 2, "name": "Contact", "item": f"{SITE}/contact.html"}
                ]
            },
            {
                "@type": "FAQPage",
                "@id": f"{SITE}/contact.html#faq",
                "url": f"{SITE}/contact.html#faq",
                "name": "Frequently asked questions about working with VIRELEO",
                "isPartOf": {"@id": f"{SITE}/contact.html#webpage"},
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "What information should I prepare before contacting VIRELEO?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Share a brief overview of your product idea, target audience, core features or required integrations, and your desired launch timeline. A high-level concept is enough to initiate the discovery review."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "How quickly does VIRELEO respond to project inquiries?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "VIRELEO reviews and responds to project inquiries sent through the contact form, email, or WhatsApp within 24 business hours with initial technical feedback and scheduling options for an architecture call."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Does VIRELEO sign Non-Disclosure Agreements (NDAs)?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Yes. VIRELEO routinely signs mutual Non-Disclosure Agreements before reviewing proprietary project specifications, database architectures, or business workflows."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "What engagement models and payment terms does VIRELEO offer?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "VIRELEO primarily offers milestone-based fixed-price contracts for custom websites, SaaS MVPs, and mobile applications. Dedicated monthly engineering retainers are available for ongoing automation maintenance and iterative feature sprints."
                        }
                    }
                ]
            }
        ]
    elif file == 'work.html':
        graph = [
            org,
            website,
            {
                "@type": "CollectionPage",
                "@id": f"{SITE}/work.html#webpage",
                "url": f"{SITE}/work.html",
                "name": "Selected Projects & Engineering Case Studies | VIRELEO",
                "isPartOf": {"@id": site_id},
                "about": {"@id": org_id},
                "breadcrumb": {"@id": f"{SITE}/work.html#breadcrumb"},
                "mainEntity": {"@id": f"{SITE}/work.html#projects"}
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{SITE}/work.html#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                    {"@type": "ListItem", "position": 2, "name": "Work", "item": f"{SITE}/work.html"}
                ]
            },
            {
                "@type": "ItemList",
                "@id": f"{SITE}/work.html#projects",
                "name": "VIRELEO selected projects",
                "numberOfItems": 8,
                "itemListOrder": "https://schema.org/ItemListOrderAscending",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "item": {
                            "@type": "CreativeWork",
                            "@id": "https://appliory.tech/#project",
                            "name": "Appliory",
                            "description": "A web platform providing free document checking, PDF management and image processing tools directly in the browser.",
                            "url": "https://appliory.tech/",
                            "image": f"{SITE}/images/projects/appliory.jpg",
                            "creator": {"@id": org_id}
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "item": {
                            "@type": "CreativeWork",
                            "@id": "https://ammar-portfolio-web.netlify.app/#project",
                            "name": "Ammar Portfolio",
                            "description": "A responsive personal portfolio presenting skills, projects and contact details in a clean, fast layout.",
                            "url": "https://ammar-portfolio-web.netlify.app/",
                            "image": f"{SITE}/images/projects/ammar-portfolio.jpg",
                            "creator": {"@id": org_id}
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "item": {
                            "@type": "CreativeWork",
                            "@id": "https://lean-canvas-model.netlify.app/#project",
                            "name": "Lean Canvas Model",
                            "description": "A web tool for laying out a business idea on the Lean Canvas, including its problem, solution, customers and revenue.",
                            "url": "https://lean-canvas-model.netlify.app/",
                            "image": f"{SITE}/images/projects/lean-canvas-model.jpg",
                            "creator": {"@id": org_id}
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 4,
                        "item": {
                            "@type": "CreativeWork",
                            "@id": f"{SITE}/work.html#whatsapp-dm-automation",
                            "name": "WhatsApp DM Automation",
                            "description": "Automated replies, lead capture and booking flows that run inside WhatsApp conversations.",
                            "image": f"{SITE}/images/projects/whatsapp-dm-wide.jpg",
                            "creator": {"@id": org_id}
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 5,
                        "item": {
                            "@type": "CreativeWork",
                            "@id": f"{SITE}/work.html#instagram-dm-automation",
                            "name": "Instagram DM Automation",
                            "description": "Automated, consistent answers to Instagram direct messages so new enquiries are not left waiting.",
                            "image": f"{SITE}/images/projects/instagram-dm-wide.jpg",
                            "creator": {"@id": org_id}
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 6,
                        "item": {
                            "@type": "CreativeWork",
                            "@id": f"{SITE}/work.html#iot-weather-hailstorm-protection",
                            "name": "IoT Weather and Hailstorm Protection System",
                            "description": "A mobile app connected to IoT sensors that tracks local weather and warns of incoming hailstorms.",
                            "image": f"{SITE}/images/projects/iot-weather.jpg",
                            "creator": {"@id": org_id}
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 7,
                        "item": {
                            "@type": "CreativeWork",
                            "@id": "https://ai-employee-os-lhqy.vercel.app/#project",
                            "name": "AI Employee OS",
                            "description": "An AI-powered workspace that takes on routine business tasks like an additional member of the team.",
                            "url": "https://ai-employee-os-lhqy.vercel.app/",
                            "image": f"{SITE}/images/projects/ai-employee-os.jpg",
                            "creator": {"@id": org_id}
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 8,
                        "item": {
                            "@type": "CreativeWork",
                            "@id": "https://email-intelligence-system-seven.vercel.app/#project",
                            "name": "MailNexa AI",
                            "description": "An email intelligence system that sorts incoming mail, summarizes it and helps users respond faster.",
                            "url": "https://email-intelligence-system-seven.vercel.app/",
                            "image": f"{SITE}/images/projects/mailnexa-ai.jpg",
                            "creator": {"@id": org_id}
                        }
                    }
                ]
            }
        ]
    else:
        graph = [org, website]
        page = {
            "@type": ptype,
            "@id": url + '#webpage',
            "url": url,
            "name": title,
            "description": desc,
            "inLanguage": "en",
            "isPartOf": {
                "@type": "WebSite",
                "@id": site_id,
                "url": SITE + '/',
                "name": "VIRELEO"
            },
            "about": {"@id": org_id},
            "mainEntity": {"@id": org_id},
            "primaryImageOfPage": {
                "@type": "ImageObject",
                "url": SITE + '/images/og-image.jpg'
            },
            "speakable": {
                "@type": "SpeakableSpecification",
                "cssSelector": ["h1", ".hero2-lead", ".section-title", "h2"]
            }
        }
        if crumb:
            page["breadcrumb"] = {"@id": url + '#breadcrumb'}
            graph.append({
                "@type": "BreadcrumbList",
                "@id": url + '#breadcrumb',
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + '/'},
                    {"@type": "ListItem", "position": 2, "name": crumb, "item": url}
                ]
            })
        service_pages = {
            'website-development.html': ('Custom Website Development Services', 'Custom-coded business websites, web applications, landing pages, and scalable e-commerce storefronts.'),
            'app-development.html': ('Mobile App & SaaS MVP Development', 'End-to-end iOS, Android, cross-platform mobile apps, cloud web applications, and production-ready SaaS MVPs.'),
            'ai-automation.html': ('AI Workflow Automation Agency', 'AI-assisted workflows for lead routing, information processing, notifications, and connected autonomous systems.'),
            'ai-chatbots.html': ('Custom AI Chatbot Development', 'Website, WhatsApp Business API, and Instagram DM chatbot automation for 24/7 customer support and lead qualification.'),
        }
        if file in service_pages:
            n, d = service_pages[file]
            page['mainEntity'] = {
                '@type': 'Service',
                'name': n,
                'description': d,
                'provider': {'@id': org_id},
                'serviceType': n,
                'areaServed': 'Worldwide'
            }
        if ptype == 'BlogPosting':
            page["headline"] = title
            page["author"] = {
                "@type": "Person",
                "name": "Ammar Hassan Malik",
                "jobTitle": "Founder & Lead Engineer",
                "url": SITE + "/about.html"
            }
            page["publisher"] = {"@id": org_id}
            page["datePublished"] = "2026-11-01"
            page["dateModified"] = TODAY

        if file == 'blog-cost-to-build-saas-mvp.html':
            graph.append({
                "@type": "FAQPage",
                "@id": url + '#faq',
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "How much does it cost to build a SaaS MVP in 2026?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Building a custom, production-grade SaaS Minimum Viable Product (MVP) in 2026 typically costs between $4,500 and $12,000 with a delivery timeline of 4 to 8 weeks. A focused micro-SaaS starts at $4,500–$6,500, a standard multi-tenant B2B platform costs $7,500–$11,000, and an AI-powered SaaS platform ranges between $9,000 and $14,000."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "What are the ongoing monthly infrastructure costs for a SaaS MVP after launch?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "A modern lean SaaS MVP built on modern cloud services typically incurs $45 to $75 per month in operating expenses: Vercel/Cloudflare hosting ($20/mo), Supabase/Neon PostgreSQL database ($25/mo), Resend transactional email ($0–$15/mo), and Stripe fees (2.9% + 30¢ per transaction only when revenue is generated)."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Do I own 100% of the source code after development?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Yes, absolutely. Upon completion, full intellectual property, Git repositories, deployment configurations, and database credentials are transferred directly to your organization with zero recurring platform or agency license fees."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Why is a custom-coded SaaS MVP better than building on No-Code tools like Bubble?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Custom-coded SaaS apps (built with Next.js, Node.js, and PostgreSQL) offer zero vendor lock-in, sub-second response times, full IP ownership for investors, predictable cloud hosting costs, and unlimited scalability. No-code tools frequently impose severe database query limits, vendor lock-in, and steep tiered pricing once user traffic increases."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "How much does an AI-powered SaaS MVP cost compared to standard software?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "An AI-powered SaaS MVP typically costs between $9,000 and $14,000. The additional engineering covers OpenAI/Claude API integration, streaming responses, vector database embeddings (Pinecone/pgvector), asynchronous worker queues, and prompt token caching."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Can I build a SaaS MVP for under $5,000?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Yes — if the scope is tightly focused. A micro-SaaS with a single core workflow with passwordless auth and Stripe billing can be engineered for $4,500 to $5,500 in 3 to 4 weeks. The key is strict scoping: build only the single high-value workflow needed to sign up paying early adopters."
                        }
                    }
                ]
            })

        if file == 'blog-cost-to-build-an-mvp.html':
            graph.append({
                "@type": "FAQPage",
                "@id": url + '#faq',
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "How much does an MVP cost to build in 2026?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "In 2026, building a custom Minimum Viable Product (MVP) typically costs between $3,500 and $12,000 for early-stage startups. A simple web app prototype costs $3,500–$5,500, a cross-platform mobile app MVP costs $5,500–$9,500, and a multi-sided marketplace or hardware/IoT software platform ranges between $7,500 and $12,000."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "How long does it take to develop a startup MVP?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "A focused MVP should take between 4 and 8 weeks to design, develop, and deploy. If an agency quotes 4 to 6 months for an MVP, the scope is too broad. Real MVPs test one core hypothesis with real users as quickly as possible."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "What is the difference between an MVP and a prototype?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "A prototype is a clickable design or non-functional visual mockup used to demonstrate an idea. An MVP (Minimum Viable Product) is fully functional, production-deployed software with real user accounts, live database storage, and actual data workflows that customers can use and pay for."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "How should founders allocate their MVP budget?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Founders should allocate 60% of their seed budget to custom core engineering and database architecture, 20% to UX design and responsive interfaces, 10% to QA testing and cloud deployment, and reserve the remaining 10% for post-launch user feedback iterations."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Do I retain full code ownership after the project?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Yes. With VIRELEO, you retain 100% intellectual property ownership. Private GitHub repositories, database credentials, and production deployment pipelines are handed over directly to your team upon completion."
                        }
                    }
                ]
            })
        graph.append(page)

    ld = json.dumps([{"@context": "https://schema.org", "@graph": graph}], indent=2, ensure_ascii=False)
    return (
        f'<!--seo:start-->\n'
        f'<link rel="canonical" href="{url}">\n'
        f'<meta property="og:url" content="{url}">\n'
        f'<meta property="og:type" content="website">\n'
        f'<meta property="og:site_name" content="VIRELEO">\n'
        f'<meta property="og:title" content="{title}">\n'
        f'<meta property="og:description" content="{desc}">\n'
        f'<meta property="og:image" content="{SITE}/images/og-image.jpg">\n'
        f'<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{title}">\n'
        f'<meta name="twitter:description" content="{desc}">\n'
        f'<meta name="twitter:image" content="{SITE}/images/og-image.jpg">\n'
        f'<script type="application/ld+json">\n{ld}\n</script>\n'
        f'<!--seo:end-->'
    )

FAVICON_BLOCK = (
    f'<link rel="icon" type="image/png" sizes="48x48" href="{SITE}/favicon-48.png">\n'
    f'<link rel="icon" type="image/png" sizes="192x192" href="{SITE}/icon-192.png">\n'
    f'<link rel="icon" type="image/png" sizes="512x512" href="{SITE}/icon-512.png">\n'
    f'<link rel="shortcut icon" href="{SITE}/favicon.ico">\n'
    f'<link rel="icon" href="{SITE}/favicon.ico" sizes="any">\n'
    f'<link rel="apple-touch-icon" sizes="180x180" href="{SITE}/apple-touch-icon.png">\n'
    f'<link rel="manifest" href="/site.webmanifest">\n'
    f'<meta name="msapplication-TileColor" content="#0a0f1f">'
)

for file, path, ptype, crumb, priority, changefreq in PAGES:
    p = ROOT / file
    if not p.exists():
        continue
    h = p.read_text(encoding='utf-8')
    title_match = re.search(r'<title>(.*?)</title>', h, re.S)
    title = title_match.group(1).strip() if title_match else 'VIRELEO'
    desc_match = re.search(r'<meta name="description" content="(.*?)"', h)
    desc = desc_match.group(1).strip() if desc_match else ''

    # Clean legacy static Organization block if any
    h = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "Organization".*?</script>\s*', '', h, count=1, flags=re.S)

    # Standardize favicon links with absolute URLs
    h = re.sub(
        r'<link rel="(?:shortcut )?icon".*?>\s*(?:<link rel="(?:shortcut )?icon".*?>\s*)*(?:<link rel="apple-touch-icon".*?>\s*)*(?:<link rel="manifest".*?>\s*)*(?:<meta name="msapplication-TileColor".*?>\s*)?',
        FAVICON_BLOCK + '\n',
        h,
        count=1,
        flags=re.S
    )

    # Build and insert SEO block
    block = build_block(file, path, ptype, crumb, title, desc)
    if '<!--seo:start-->' in h:
        h = re.sub(r'<!--seo:start-->.*?<!--seo:end-->', lambda m: block, h, count=1, flags=re.S)
    else:
        h = h.replace('</head>', block + '\n</head>', 1)

    p.write_text(h, encoding='utf-8')
    print('updated', file)

# Generate Sitemap with proper XML namespaces, priorities, and changefreq
sitemap_urls = []
for file, path, _, _, priority, changefreq in PAGES:
    url_entry = (
        f'  <url>\n'
        f'    <loc>{SITE}{path}</loc>\n'
        f'    <lastmod>{TODAY}</lastmod>\n'
        f'    <changefreq>{changefreq}</changefreq>\n'
        f'    <priority>{priority}</priority>\n'
        f'  </url>\n'
    )
    sitemap_urls.append(url_entry)

sitemap_xml = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(sitemap_urls)
    + '</urlset>\n'
)
(ROOT / 'sitemap.xml').write_text(sitemap_xml, encoding='utf-8')

# Ensure robots.txt points to correct sitemap and allows Googlebot-Favicon
r = (ROOT / 'robots.txt').read_text(encoding='utf-8')
if 'Googlebot-Favicon' not in r:
    r = re.sub(r'(User-agent: Googlebot\s*\nAllow: /)', r'\1\n\nUser-agent: Googlebot-Favicon\nAllow: /', r)
r = re.sub(r'^#?\s*Sitemap:.*$', '', r, flags=re.M).rstrip() + f'\n\nSitemap: {SITE}/sitemap.xml\n'
(ROOT / 'robots.txt').write_text(r, encoding='utf-8')

print('sitemap.xml and robots.txt successfully updated for', SITE)

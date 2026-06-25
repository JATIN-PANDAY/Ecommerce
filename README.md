# 🛒 Eflyer — E-commerce Platform

> A scalable, full-featured e-commerce web application built with Django — featuring user authentication, product management, online payment integration, and secure order handling.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2.4-092E20?style=flat&logo=django&logoColor=white)
![Instamojo](https://img.shields.io/badge/Payment-Instamojo-F97316?style=flat)
![REST API](https://img.shields.io/badge/API-REST-0EA5E9?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

---

## 📌 Overview

**Eflyer** is a production-ready e-commerce platform that handles the complete online shopping lifecycle — from product browsing and cart management to secure payment processing and order tracking. Built with Django on the backend and integrated with **Instamojo** payment gateway for real-world transaction handling.

The platform is designed with scalability and security in mind, offering clean REST APIs for transaction management and an optimized database layer for fast product discovery.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🔐 **User Authentication** | Secure registration, login, logout with session management |
| 🛍️ **Product Management** | Add, update, delete products with image support via Pillow |
| 🔍 **Search & Filtering** | Advanced product search and category-based filtering |
| 💳 **Payment Gateway** | Integrated Instamojo for real online payment processing |
| 📦 **Order Management** | Complete order lifecycle — place, track, and manage orders |
| 🔗 **REST APIs** | Clean REST endpoints for transactions and order management |
| 🗄️ **Optimized Database** | Efficient query design for fast product and order retrieval |
| 📱 **Responsive UI** | Mobile-friendly interface for seamless shopping experience |

---

## 🛠️ Tech Stack

### Backend
- **Python 3.10+** — Core language
- **Django 4.2.4** — Web framework (ORM, views, authentication, admin)
- **SQLite** — Development database
- **Django REST Framework** — REST API development

### Payment Integration
- **Instamojo Wrapper 1.2.0** — Payment gateway for secure online transactions
- **Requests 2.31.0** — HTTP client for payment API communication

### Media & File Handling
- **Pillow 10.0.0** — Product image upload and processing

### Frontend
- **HTML5 / CSS3** — Responsive templates
- **Django Template Engine** — Dynamic page rendering

---

## 🏗️ System Architecture

```
User Request
     │
     ▼
Django Views (Authentication Check)
     │
     ├──► Product Module   →  Search, Filter, Detail, Cart
     │
     ├──► Order Module     →  Place Order, Order History
     │
     ├──► Payment Module   →  Instamojo Gateway → Payment Verify
     │
     └──► REST API Layer   →  Transaction & Order Endpoints
                                      │
                                      ▼
                               Django ORM → SQLite DB
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip
- Git
- Instamojo account (for payment integration)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/eflyer-ecommerce.git
cd eflyer-ecommerce

# 2. Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Add your Instamojo API key and salt in .env
```

### Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
INSTAMOJO_API_KEY=your_instamojo_api_key
INSTAMOJO_AUTH_TOKEN=your_instamojo_auth_token
INSTAMOJO_PRIVATE_SALT=your_private_salt
```

### Run the Project

```bash
# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create admin superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

Open your browser at **http://127.0.0.1:8000**

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/products/` | List all products |
| `GET` | `/api/products/?search=keyword` | Search products |
| `GET` | `/api/products/?category=id` | Filter by category |
| `POST` | `/api/orders/create/` | Place a new order |
| `GET` | `/api/orders/<id>/` | Get order details |
| `POST` | `/api/payment/initiate/` | Initiate payment via Instamojo |
| `POST` | `/api/payment/verify/` | Verify payment callback |

---

## 💳 Payment Flow

```
User Checkout
     │
     ▼
Order Created (status: pending)
     │
     ▼
Instamojo Payment Link Generated
     │
     ▼
User Completes Payment on Instamojo
     │
     ▼
Webhook Callback → Payment Verified
     │
     ▼
Order Status Updated (status: confirmed)
     │
     ▼
Confirmation shown to User
```

---

## 📦 Requirements

Key packages used:

```
Django==4.2.4
instamojo-wrapper==1.2.0
Pillow==10.0.0
requests==2.31.0
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🎯 Use Case

Eflyer is suitable for:
- Small to medium online retail stores
- College/academic e-commerce projects needing real payment integration
- Developers learning Django + payment gateway integration
- Businesses wanting a customizable Django-based shopping platform

---

## 🙋‍♂️ Author

**Jatin Panday**
- 📧 jatinpanday136@gmail.com
- 💼 [LinkedIn](https://www.linkedin.com/in/jatin-panday/)
- 🐙 [GitHub](https://github.com/JATIN-PANDAY)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> ⭐ If you found this project useful, please consider giving it a star on GitHub!

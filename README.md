# HipHopz - Full Stack E-commerce Platform
A comprehensive e-commerce web application built with Django framework following the Model-View-Template (MVT) architecture. HipHopz provides a complete online shopping experience with advanced features for both customers and administrators.

🚀 Features

## Customer Features

### User Authentication & Management
- User registration with email verification
- Secure login/logout system
- Password reset functionality
- Profile management with address book
- User dashboard with order history

### Product Browsing & Search
- Advanced filtering (category, brand, price range, colors, sizes)
- Product search functionality
- Sort products (A-Z, price, popularity, latest)
- Product details with multiple images
- Product ratings and reviews
- Wishlist functionality

### Shopping Experience
- Add to cart with quantity management
- Real-time cart updates
- Shopping cart persistence
- Multiple payment options integration
- Secure checkout process

### Order Management
- Order tracking and management
- Order history with detailed information
- Order status updates
- Invoice generation
- Customer support integration

## Admin Features

### Dashboard Analytics
- Sales charts and revenue tracking
- Order status analytics
- Top-selling products and categories
- Customer insights and reports
- Customizable date filtering

### Product Management
- Add/edit products with image management
- Multi-variant products (size, color, quantity)
- Category and subcategory management
- Inventory tracking and alerts
- Bulk product operations

### Order Processing
- Order status management
- Customer order oversight
- Sales reporting and analytics
- Payment tracking
- Shipping management

### Offers & Promotions
- Discount management system
- Promotional campaigns
- Seasonal offers
- Customer-specific deals
- Coupon code generation

🛠️ Technology Stack
- **Backend**: Django, Python
- **Database**: SQLite/PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Payment Integration**: Multiple payment gateways
- **Authentication**: Django built-in auth system
- **Media Handling**: Django file handling
- **Charts & Analytics**: Chart.js

📦 Project Structure
```
HipHopz/
├── Admin/              # Admin management & dashboard
├── cart/               # Shopping cart functionality
├── offer/              # Offers & promotions management
├── order/              # Order processing & management
├── products/           # Product catalog & management
├── Userapp/           # User authentication & profiles
├── static/            # Static files (CSS, JS, images)
├── templates/         # HTML templates
├── media/             # User uploaded files
└── shopifyproject/    # Project configuration & settings
```

🚀 Installation & Setup

## Prerequisites
- Python 3.8+
- Git
- Virtual environment tool

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jasir-p/ecomerce.git
   cd HipHopz
   ```

2. **Create virtual environment**
   ```bash
   python -m venv env
   source venv/bin/activate  # On Windows: hiphopz_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file with the following variables:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password
   PAYMENT_API_KEY=your_payment_key
   PAYMENT_API_SECRET=your_payment_secret
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run the application**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   Visit `http://127.0.0.1:8000/` to access HipHopz.

🏗️ App Structure

### Core Applications

- **Admin**: Administrative dashboard and management tools
- **cart**: Shopping cart functionality and session management
- **offer**: Promotional offers, discounts, and coupon management
- **order**: Order processing, tracking, and management
- **products**: Product catalog, categories, and inventory
- **Userapp**: User authentication, profiles, and account management

### Configuration
- **shopifyproject**: Main project settings and URL configurations
- **static**: Static assets (CSS, JavaScript, images)
- **templates**: HTML templates for all apps

💳 Payment Integration
HipHopz supports multiple payment methods:
- Credit/Debit cards
- Digital wallets
- Net banking
- Cash on Delivery (COD)
- UPI payments

🛒 Shopping Features
- **Smart Cart**: Persistent shopping cart with real-time updates
- **Wishlist**: Save items for later purchase
- **Quick Buy**: Express checkout for faster purchases
- **Product Comparison**: Compare multiple products
- **Recently Viewed**: Track browsing history

📊 Key Highlights
- **Responsive Design**: Mobile-friendly interface across all devices
- **Modular Architecture**: Well-organized Django apps for scalability
- **Admin Dashboard**: Comprehensive management tools
- **User Experience**: Intuitive and modern UI/UX
- **Security**: Built-in Django security features
- **Performance**: Optimized for fast loading times

🔒 Security Features
- CSRF protection
- User authentication & authorization
- Secure session management
- Password encryption
- Form validation
- XSS protection

📈 Admin Analytics
- Sales performance tracking
- Customer behavior insights
- Product popularity metrics
- Revenue analytics
- Order fulfillment statistics

🚀 Deployment Ready
Configured for easy deployment with:
- Environment-based configuration
- Static file management
- Database migrations
- Production settings
- Error handling

👨‍💻 Developer
**Your Name** - Full Stack Developer
- GitHub: [@jasir-p](https://github.com/jasir-p)
- Email: jazjasir7@gmail.com

🤝 Contributing
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

🐛 Bug Reports
If you find a bug, please create an issue on GitHub with:
- Bug description
- Steps to reproduce
- Expected behavior
- Screenshots (if applicable)

📞 Support
For support and questions:
- Email: support@hiphopz.com
- GitHub Issues: [Create an issue](https://github.com/Jasir-p/ecomerce)

---

**HipHopz - Your Ultimate E-commerce Solution!** 🛒✨

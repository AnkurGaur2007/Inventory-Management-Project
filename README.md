# 📦 Inventory Management System (IMS)

A simple **command-line based Inventory Management System** built in Python using CSV files for data storage.
This project allows users to manage products, track inventory, and generate customer bills efficiently.

---

## 🚀 Project Overview

This system provides two main modules:

* 🧾 **Inventory Management**
* 💰 **Billing System**

All data is stored locally using `.csv` files, making it lightweight and easy to use without requiring a database.

---

## ✨ Features

### 📦 Inventory Module

* ➕ Add new products
* 📋 View all products
* 🔍 Search product by ID

### 💰 Billing Module

* 🧾 Create new bills
* 📄 View all bills
* 🔍 Search bills by Customer ID or Name
* 📉 Automatically updates inventory after purchase

---

## 🏗️ Project Structure

```
.
├── main.py / app.py        # Main Python script
├── records.csv            # Stores product inventory
├── billing.csv            # Stores billing records
├── README.md              # Documentation
```

---

## ⚙️ Technologies Used

* **Python**
* **CSV (Comma-Separated Values)** for data storage
* **Datetime module** for bill date tracking

---

## 🧠 How It Works

### 1. Inventory System

* Products are stored in `records.csv`
* Each product contains:

  * Product ID
  * Name
  * Company
  * Expiry Date
  * Price
  * Quantity

---

### 2. Billing System

* Bills are stored in `billing.csv`
* Each bill contains:

  * Customer ID
  * Name
  * Mobile Number
  * Bill Date
  * Total Amount

---

### 3. Workflow

1. User selects Inventory or Billing
2. Performs operations (add/search/view)
3. While billing:

   * Product is selected
   * Quantity is deducted from inventory
   * Total bill is calculated
4. Bill is saved automatically

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

``` 
git clone https://github.com/your-username/inventory-management-system.git
cd inventory-management-system
```

---

### 2. Run the Program

``` 
python main.py
```

*(Replace `main.py` with your actual file name if different)*

---

## ▶️ Usage

### Start Menu

```
1. Access Inventory
2. Access Billing
3. Exit
```

---

### Inventory Options

```
1. Enter New Product
2. Show Inventory
3. Search Product
4. Back
```

---

### Billing Options

```
1. Make New Bill
2. Print All Bills
3. Search Bill
4. Back
```

---

## 📂 Data Storage

* `records.csv` → Stores product details
* `billing.csv` → Stores customer billing data

If these files do not exist, they are automatically created when needed.

---

## ⚠️ Limitations

* No graphical user interface (CLI only)
* No database (uses CSV files)
* No authentication system
* Minimal error handling for invalid inputs
* Not suitable for large-scale applications

---

## 🔮 Future Improvements

* 🖥️ Add GUI (Tkinter / Web App)
* 🗄️ Integrate database (MySQL / SQLite)
* 🔐 Add user authentication
* 📊 Generate reports and analytics
* 🧾 Print/download invoices
* ⚡ Improve error handling

---

## 🤝 Contributing

Contributions are welcome!

* Fork the repository
* Create a new branch
* Submit a pull request

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

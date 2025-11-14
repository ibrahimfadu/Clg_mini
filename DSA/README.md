# Food Delivery Platform – C Project

This project simulates a simple **food delivery platform** like Zomato/Swiggy using **Data Structures in C**.  
It demonstrates real-world usage of queues, BSTs, structures, and modular programming.

---

## 📌 Features

### ✔ Place Order
User enters:
- Restaurant name  
- Customer name  
- Preparation time  

Order goes into **Pending Queue**.

### ✔ Prepare Order
Moves the first pending order into **Ready Queue**.

### ✔ Assign Delivery Agent
Moves one order from **Ready → In-Transit BST** and assigns:
- Random delivery agent ID  
- Random ETA (10–45 min)

BST stores orders **sorted by ETA**.

### ✔ Track Order
Searches:
- Ready Queue  
- In-Transit BST  

Then prints current status.

### ✔ Generate Platform Report
Shows:
- Total pending orders  
- Total ready orders  
- In-transit orders (sorted by ETA)

### ✔ Cleanup
Frees all dynamic memory used by queues and BST.

---

## 📁 Project Structure

project/
│
├── include/
│ ├── delivery.h
│ ├── queue.h
│ └── bst.h
│
├── src/
│ ├── delivery.c
│ ├── queue.c
│ ├── bst.c
│
├── main.c
└── README.md



---

## 🚀 How to Compile

Run this command inside your project folder:

```sh
gcc -o app src/*.c main.c -I include

Run the program:

./app


🧠 Data Structures Used
Queue

Used for:

Pending Orders

Ready Orders

Operations:

enqueue

dequeue

is_empty

size

Binary Search Tree (BST)

Used for:

In-transit deliveries sorted by ETA

Operations:

insert

search

inorder traversal

delete


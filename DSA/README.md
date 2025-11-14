# Food Delivery Platform – C Project

This project simulates a simplified Zomato/Swiggy-like food delivery platform using Data Structures in C.
It demonstrates real-world usage of:

Queues → handling pending & ready orders

Binary Search Tree (BST) → tracking in-transit orders sorted by ETA

Structures → Orders, Delivery Agents, Platform

Dynamic Memory Allocation

Modular Programming (multiple C files)

📌 Features
✔ Place Order

User enters:

Restaurant name

Customer name

Preparation time

Order is added to Pending Queue.

✔ Prepare Order

Moves one order from Pending → Ready
(simulates cooking/preparation).

✔ Assign Delivery Agent

Moves one order from Ready → BST (In-Transit) and assigns:

Random delivery agent ID

Random ETA (10–45 minutes)

BST stores orders sorted by ETA, so the fastest orders appear first.

✔ Track Order

Searches both:

Ready Queue

In-Transit BST

Shows the current status.

✔ Platform Report

Displays total:

Pending orders

Ready orders

In-transit orders (in sorted ETA order)

✔ Cleanup

Free all dynamic memory (queues + BST).

📁 Project Structure


project/
│
├── include/
│   ├── delivery.h
│   ├── queue.h
│   └── bst.h
│
├── src/
│   ├── delivery.c
│   ├── queue.c
│   ├── bst.c
│
├── main.c
└── README.md


How to Compile

Make sure you are inside the project folder.

Compile all .c files:

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

BST (Binary Search Tree)

Used for:

In-transit delivery tracking

Sorted by:

ETA (Estimated Time of Arrival)

Operations:

insert

search

inorder traversal

delete

🔧 Future Enhancements

Delivery completion

Distance calculation

Alternative route suggestion

Multiple agents

File storage for orders

Graph-based routing system

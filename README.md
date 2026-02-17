Group Project: Data Structures & Algorithms using python

Title
Implementation and Application of Data Structures and Algorithms Using python 

1.	Introduction
In computer science, data structures and algorithms are the foundation of efficient software systems. Data structures define how data is organized and stored in memory, while algorithms define the steps used to process that data. Choosing an appropriate data structure and algorithm directly affect system performance, memory usage, and scalability.
This assignment demonstrates different classifications and types of data structures using the python programming language. It further explores where these data structures are applied in real-world systems like YouTube, Facebook, and operating systems, the algorithms that operate on them, and how both data structures and algorithms work together inside a computer system.

2. Classification of Data Structures
From our understanding, data structures can be grouped into two main categories:
•	Primitive Data Structures
•	Non-Primitive Data Structures
Non-primitive data structures can further be divided into:
•	Linear data structures
•	Non-linear data structures
This classification helps programmers choose the most suitable structure depending on how data needs to be organized and accessed.

3. Primitive Data Structures
Primitive data structures store single, simple values. They form the building blocks of more complex data structures.

Examples
•	Integer (int)
•	Floating point (float)
•	Character (char)

Applications and Reasons
Primitive data structures are used in:
•	Inventory systems
•	Student grading systems
•	Banking applications
We found that they are preferred because they consume less memory and allow very fast processing of simple data values.

4.Non-Primitive Data Structures
Non-primitive data structures store collections of data and are used when handling larger or more complex information.

4.1 Linear Data Structures
Linear data structures arrange elements in a sequential order.

4.1.1 Arrays

Definition:
An array is a collection of elements of the same type stored at contiguous memory locations. It allows random access using indices.

Applications & Why:
•	Used in image processing (pixels stored in arrays).
•	Applied in scientific simulations (large datasets indexed).
Arrays are chosen because they allow fast random access.

Real-world Examples & Reasons:
•	YouTube video frames are stored as arrays of pixels → arrays allow quick rendering of millions of pixels per frame.
•	Excel spreadsheets internally use arrays → arrays make it easy to access cells by row/column indices.


4.1.2 Linked List

Definition:
A linked list is a linear data structure where elements (nodes) are connected using pointers. Each node contains data and a reference to the next node.

Applications & Why:
•	Music playlists (songs linked one after another).
•	Undo/Redo functionality in text editors.
Linked lists are chosen because they allow dynamic memory allocation and easy insertion/deletion.
Real-world Examples & Reasons:
•	Spotify playlists → linked lists make it easy to add/remove songs dynamically.
•	Microsoft Word → undo/redo operations rely on linked lists to track changes in sequence.

4.1.3 Stack

Definition:
A stack is a linear data structure that follows LIFO (Last In First Out). Insertions and deletions happen at one end (the top).

Applications & Why:
•	Browser history navigation (back/forward).
•	Expression evaluation in compilers.
Stacks are chosen because they naturally handle nested operations.
Real-world Examples & Reasons:
•	Google Chrome → stack stores visited pages so users can go back/forward easily.
•	Java compilers → stacks evaluate nested expressions during code compilation.

4.1.4 Queue

Definition:
A queue is a linear data structure that follows FIFO (First In First Out). Insertions happen at the rear, deletions at the front.

Applications & Why:
•	Print spooling (jobs queued for printer).
•	Customer service systems (FIFO order).
Queues are chosen because they ensure fairness in serving requests.
Real-world Examples & Reasons:
•	Netflix streaming servers → queues manage millions of user requests fairly.
•	Operating systems → queues schedule processes so each gets CPU time in order.

4.2 Non-Linear Data Structures
Non-linear data structures organize data in a hierarchical or interconnected manner.

4.2.1 Trees

Definition:
A tree is a hierarchical data structure with nodes connected in parent-child relationships. The top node is the root, and bottom nodes are leaves.

Applications & Why:
•	File systems (folders and subfolders).
•	Decision-making in AI (decision trees).
Trees are chosen because they represent hierarchical data.
Real-world Examples & Reasons:
•	Windows Explorer → tree structure organizes files/folders.
•	Google Search ranking → decision trees classify and rank results efficiently.

4.2.2 Graphs

Definition:
A graph is a set of vertices connected by edges. Unlike trees, graphs can have cycles.

Applications & Why:
•	Social networks (users as nodes, friendships as edges).
•	Navigation systems (cities as nodes, roads as edges).
Graphs are chosen because they capture relationships and connectivity.
Real-world Examples & Reasons:
•	Facebook → graphs model friendships and connections.
•	Google Maps → graphs represent cities and roads for route finding.
•	LinkedIn → graphs represent professional networks, showing how people are connected.

5. Algorithms in Action
•	Sorting (Quick Sort, Merge Sort): Used in Amazon to display products by price.
•	Searching (Binary Search): Used in databases for fast retrieval.
•	Merging: Used in Excel when combining datasets.
. How Data Structures & Algorithms Work in Systems
From our research, we learned that data structures determine how data is stored in memory, while algorithms determine how that data is processed. A system becomes efficient only when both are chosen correctly.

For example:
•	Operating Systems: Use queues for process scheduling.
•	Compilers: Use stacks for parsing expressions.
•	Databases: Use trees (B-trees) for indexing.
•	AI Systems: Use graphs for neural networks and decision-making.

6. Conclusion
Our group concluded that data structures are not just programming topics but  they are design choices that determine whether a system is efficient or sluggish. Algorithms breathe life into these structures by defining how data is manipulated. Together, they form the invisible architecture behind modern computing, powering platforms like YouTube, Facebook, Google Maps, and Netflix.

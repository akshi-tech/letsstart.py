
#include <iostream>
using namespace std;

// Abstract Class
class Person {
protected:
    string name;

public:
    Person(string n) {
        name = n;
    }

    virtual void display() = 0; // Pure Virtual Function
};

// Base Class
class Student : public Person {
private:
    int marks; // Encapsulation

public:
    // Constructor
    Student(string n, int m) : Person(n) {
        marks = m;
    }

    // Function Overloading
    void show() {
        cout << "Student Name: " << name << endl;
    }

    void show(int x) {
        cout << "Marks: " << marks + x << endl;
    }

    // Virtual Function
    void display() override {
        cout << "Name: " << name
             << ", Marks: " << marks << endl;
    }

    // Friend Function
    friend void result(Student s);

    // Operator Overloading
    Student operator+(Student s) {
        return Student(name, marks + s.marks);
    }

    // Destructor
    ~Student() {
        cout << "Destructor Called for " << name << endl;
    }
};

// Derived Class (Inheritance)
class Monitor : public Student {
private:
    int section;

public:
    Monitor(string n, int m, int s)
        : Student(n, m) {
        section = s;
    }

    void display() override { // Runtime Polymorphism
        cout << "Monitor Details" << endl;
        Student::display();
        cout << "Section: " << section << endl;
    }
};

// Friend Function Definition
void result(Student s) {
    cout << "Friend Function Accessing Data" << endl;
    s.display();
}

int main() {

    // Object Creation
    Student s1("Akshi", 85);
    Student s2("Riya", 90);

    // Function Overloading
    s1.show();
    s1.show(5);

    // Friend Function
    result(s1);

    // Operator Overloading
    Student s3 = s1 + s2;
    cout << "\nAfter Adding Marks:" << endl;
    s3.display();

    // Runtime Polymorphism
    Person *p;
    Monitor m1("Rahul", 95, 12);

    p = &m1;
    p->display();

    return 0;
}
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // Define a structure for Student
    struct Student {
        uint id;
        string name;
        uint age;
        string grade;
    }

    // Array to store students
    Student[] public students;
    uint public studentCount;

    // Receive function to accept Ether
    receive() external payable {}

    // Fallback function to handle non-empty data transactions
    fallback() external payable {}

    // Function to add a new student
    function addStudent(string memory _name, uint _age, string memory _grade) public {
        studentCount++;
        students.push(Student(studentCount, _name, _age, _grade));
    }

    // Function to get student details by ID
    function getStudent(uint _id) public view returns (uint, string memory, uint, string memory) {
        require(_id > 0 && _id <= studentCount, "Student does not exist.");
        Student memory student = students[_id - 1];
        return (student.id, student.name, student.age, student.grade);
    }

    // Function to get the total number of students
    function getTotalStudents() public view returns (uint) {
        return studentCount;
    }
}
































//students = [
//   { id: 1, name: "Alice", age: 20, grade: "A" },
//   { id: 2, name: "Bob", age: 22, grade: "B" },
//   { id: 3, name: "Charlie", age: 19, grade: "A" }
// ]

// Time Complexity: O(1)

// This function simply increments the studentCount and pushes a new Student struct to the end of the students array.
// Both operations (incrementing and appending) are constant-time operations, so the overall time complexity is 
// O(1).
// Space Complexity: O(1) per call
// Each time a new student is added, a fixed amount of space is needed to store their details.
// Since each call to addStudent adds a single new Student struct, the space complexity per call is constant, 
// O(1)
// O(1). However, in aggregate, if n students are added, the total space complexity will be 
// O(n).

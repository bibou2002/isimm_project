import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';
import { getTeachers } from '../services/TeacherServices';
import "../App.css";

const Teachers = () => {
  const [teachers, setTeachers] = useState([]);

  useEffect(() => {
   let mounted = true;
   getTeachers()
     .then(data => {
       if(mounted) {
         setTeachers(data)
       }
     })
   return () => mounted = false;
 }, [])

  return(
   <div className="container-fluid side-container">
   <div className="row side-row" >
    <p id="before-table"></p>
        <Table striped bordered hover className="react-bootstrap-table" id="dataTable">
        <thead>
            <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last name</th>
            <th>Qualification</th>
            <th>joining_date</th>
            <th>contact_details</th>
            <th>Dept</th>
            </tr>
        </thead>
        <tbody>
            {teachers.map((stu) =>
            <tr key={stu.id}>
                <td>{stu.id}</td>
                <td>{stu.first_name}</td>
                <td>{stu.last_name}</td>
                <td>{stu.qualification}</td>
                <td>{stu.joining_date}</td>
                <td>{stu.contact_details}</td>
                <td>{stu.department_name}</td>
            </tr>)}
        </tbody>
    </Table>
    </div>
  </div>
  );
};

export default Teachers;
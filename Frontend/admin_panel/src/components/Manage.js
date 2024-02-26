import React,{ useEffect, useState } from 'react';
import {Table} from 'react-bootstrap';
import {Button,ButtonToolbar } from 'react-bootstrap';
import { FaEdit } from 'react-icons/fa';
import { RiDeleteBin5Line } from 'react-icons/ri';
import { getTeachers, deleteTeacher } from '../services/TeacherServices';
import AddTeacherModal from "./AddTeahcerModal";


const Manage = () => {
    const [teachers, setTeachers] = useState([]);
    const [addModalShow, setAddModalShow] = useState(false);
    const [editModalShow, setEditModalShow] = useState(false);
    const [editTeacher, setEditTeacher] = useState([]);
    const [isUpdated, setIsUpdated] = useState(false);


useEffect(() => {
    let mounted = true;
    if(teachers.length && !isUpdated) {
     return;
     }
    getTeachers()
      .then(data => {
        if(mounted) {
          setTeachers(data)
        }
      })
    return () => {
       mounted = false;
       setIsUpdated(false);
    }
  }, [isUpdated, teachers])

const handleUpdate = (e, stu) => {
    e.preventDefault();
    setEditModalShow(true);
    setEditTeacher(stu);
};

const handleAdd = (e) => {
    e.preventDefault();
    setAddModalShow(true);
};

const handleDelete = (e, id) => {
    console.log(id)
    if(window.confirm('Are you sure ?')){
        e.preventDefault();
        deleteTeacher(id)
        .then((result)=>{
            alert(result);
            setIsUpdated(true);
        },
        (error)=>{
            alert("Failed to Delete Student");
        })
    }
};
let AddModelClose=()=>setAddModalShow(false);
let EditModelClose=()=>setEditModalShow(false);
return(
    <div className="container-fluid side-container">
    <div className="row side-row" >
    <p id="manage"></p>
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
              { teachers.map((stu) =>

              <tr key={stu.id}>
              <td>{stu.id}</td>
              <td>{stu.first_name}</td>
              <td>{stu.last_name}</td>
              <td>{stu.qualification}</td>
              <td>{stu.joining_date}</td>
              <td>{stu.contact_details}</td>
              <td>{stu.department_name}</td>
              <td>

              <Button className="mr-2" variant="danger"
                onClick={event => handleDelete(event,stu.id)}>
                    <RiDeleteBin5Line />
              </Button>
              <span>&nbsp;&nbsp;&nbsp;</span>
              <Button className="mr-2"
                onClick={event => handleUpdate(event,stu)}>
                    <FaEdit />
              </Button>
              {/*<UpdateTeacherModal show={editModalShow} student={editTeacher} setUpdated={setIsUpdated}
                          onHide={EditModelClose}></UpdateTeacherModal>*/}
            </td>
            </tr>)}
          </tbody>
        </Table>
        <ButtonToolbar>
            <Button variant="primary" onClick={handleAdd}>
            Add Teacher
            </Button>
            <AddTeacherModal show={addModalShow} setUpdated={setIsUpdated}
            onHide={AddModelClose}></AddTeacherModal>
        </ButtonToolbar>
    </div>
    </div>

);

};

export default Manage;

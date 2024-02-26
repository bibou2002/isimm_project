import React from 'react';
import { useState,useEffect } from 'react';
import {Modal, Col, Row, Form, Button} from 'react-bootstrap';
import {FormControl, FormGroup, FormLabel} from 'react-bootstrap';
import { getDepartments } from '../services/DepartmentServices';
import { addTeacher } from '../services/TeacherServices';


const AddTeacherModal = (props) => {
    const [Department, setDepartment] = useState([]);
    useEffect(() => {
        let mounted = true;
        getDepartments()
          .then(data => {
            if(mounted) {
              setDepartment(data)
            }
          })
        return () => mounted = false;
      }, [])

    
      const handleSubmit = (e) => {
        e.preventDefault();
        addTeacher(e.target)
        .then((result)=>{
            alert(result);
            props.setUpdated(true);
        },
        (error)=>{
            alert("Failed to Add Student");
        })
    }

    return(
        <div className="container">

            <Modal
                {...props}
                size="lg"
                aria-labelledby="contained-modal-title-vcenter"
                centered >

                <Modal.Header closeButton>
                    <Modal.Title id="contained-modal-title-vcenter">
                        Fill In Teacher Information
                    </Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Row>
                        <Col sm={6}>
                            <Form onSubmit={handleSubmit}>
                                <Form.Group controlId="FirstName">
                                    <Form.Label>First Name</Form.Label>
                                    <Form.Control type="text" name="FirstName" required placeholder="" />
                            </Form.Group>
                            <Form.Group controlId="LastName">
                                    <Form.Label>Last Name</Form.Label>
                                    <Form.Control type="text" name="LastName" required placeholder="" />
                            </Form.Group>
                            <Form.Group controlId="Qualification">
                                    <Form.Label>Qualification</Form.Label>
                                    <Form.Control type="text" name="Qualification" required placeholder="" />
                            </Form.Group>
                            <Form.Group controlId="Email">
                                    <Form.Label>Email</Form.Label>
                                    <Form.Control type="text" name="Email" required placeholder="" />
                            </Form.Group>
                            {/*<Form.Group controlId="Department">
                                    <Form.Label>Department</Form.Label>
                                    <Form.Control type="text" name="Course" required placeholder="" />
                            </Form.Group>*/}
                            <Form.Group controlId="Department">
                                <Form.Label>Department</Form.Label>
                                <Form.Control as="select" name="DepartmentId" required>
                                    <option value="">Select Department</option>
                                    {Department.map(department => (
                                    <option key={department.id} value={department.id}>{department.name}</option>
                                    ))}
                            </Form.Control>
                            </Form.Group>

                            <Form.Group>
                                <p></p>
                                <Button variant="primary" type="submit">
                                    Submit
                                </Button>
                            </Form.Group>
                            </Form>
                        </Col>
                    </Row>
                </Modal.Body>
                <Modal.Footer>
                <Button variant="danger" type="submit" onClick={props.onHide}>
                        Close
                </Button>

                </Modal.Footer>
            </Modal>
        </div>
    );
};

export default AddTeacherModal;
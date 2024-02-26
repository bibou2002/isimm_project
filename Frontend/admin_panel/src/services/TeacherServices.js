import axios from 'axios';

export function getTeachers() {
  return axios.get('http://127.0.0.1:8000/api/teacher')
    .then(response => response.data)
}

export function deleteTeacher(id) {
    return axios.delete('http://127.0.0.1:8000/api/teacher/' + id , {
     method: 'DELETE',
     headers: {
       'Accept':'application/json',
       'Content-Type':'application/json'
     }
    })
    .then(response => response.data)
  }


  export function addTeacher(student){
    console.log(student.DepartmentId.value);
    return axios.post('http://127.0.0.1:8000/api/teacher/', {
      first_name:student.FirstName.value,
      last_name:student.LastName.value,
      qualification:student.Qualification.value,
      contact_details:student.Email.value,
      department:student.DepartmentId.value,
    })
      .then(response=>response.data)
  }
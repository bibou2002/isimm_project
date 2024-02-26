import axios from 'axios';

export function getDepartments() {
    return axios.get('http://127.0.0.1:8000/api/department')
      .then(response => response.data)
  }
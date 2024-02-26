import logo from './logo.svg';
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navigation from './components/Navigation';
import './App.css';
import Home from "./components/Home";
import Teacher from "./components/Teacher"
import {BrowserRouter,Route,Routes} from 'react-router-dom';
import Manage from "./components/Manage";

function App() {
  return (
    <BrowserRouter>
    <Navigation />
    <Routes>
      <Route exact path="/" element={<Home/>} />
      <Route path="/teachers" element={<Teacher/>} />
      <Route path="/manage" element={<Manage/>} />
    </Routes>
  </BrowserRouter>
  );
}

export default App;



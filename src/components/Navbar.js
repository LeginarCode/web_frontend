import React from 'react'
import { Link } from 'react-router-dom';

import '../styles/navbar.scss';
export default function Navbar() {
    return (
        <div className="nav-wrapper">
            <nav className="navbar primary-nav">

                <Link to="/" className="navbar-brand">Leginar</Link>

                <div className="nav-items">
                    <ul>
                        <li className="navbar-item">Home</li>
                        <li className="navbar-item">About</li>
                        <li className="navbar-item">Services</li>
                    </ul>

                    <ul>
                        <Link to="/signin"><li className="navbar-btn" id="sign-in">Sign In</li></Link>
                        <Link to="/signup"><li className="navbar-btn" id="sign-up">Sign Up</li></Link>
                    </ul>
                </div>
            </nav>
        </div>
    )
}

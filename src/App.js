import React, { Component } from 'react'
import {hot} from "react-hot-loader"; // refresh on save, can use liveReload instead if not working
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Navbar from './components/Navbar';
import Footer from './components/Footer';

import Home from './routes/Home';

import './styles/main.scss';

class App extends Component {
    render() {
        return (
            <Router>
                <main>
                    <Navbar />
                    <Switch>
                        <Route exact path="/about">

                        </Route>
                        <Route exact path="/services">

                        </Route>
                        <Route exact path="/">
                            <Home />
                        </Route>
                    </Switch>
                    <Footer />
                </main>
            </Router>
        )
    }
}


export default hot(module)(App);
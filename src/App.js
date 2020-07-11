import React, { Component } from 'react'
import {hot} from "react-hot-loader"; // refresh on save, can use liveReload instead if not working
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Navbar from './components/Navbar';
import Footer from './components/Footer';

import Home 	from './routes/Home';
import SignUp 	from './routes/SignUp';
import SignIn 	from './routes/SignIn';
import Case 	from './routes/Case';

// Load FontAwesomeIcons
import { library } from '@fortawesome/fontawesome-svg-core';
import { faSearch } from '@fortawesome/free-solid-svg-icons';
library.add(faSearch);

import './styles/main.scss';

class App extends Component {
    render() {
        return (
            <Router>
                <main>
                    <Navbar />
					<section className="content">
	                    <Switch>
	                        <Route exact path="/about">
	
	                        </Route>
	                        <Route exact path="/services">
	
	                        </Route>
							<Route path="/case/:id">
								<Case />
							</Route>
							<Route exact path="/signup">
								<SignUp />
							</Route>
							<Route exact path="/signin">
								<SignIn />
							</Route>
	                        <Route exact path="/">
	                            <Home />
	                        </Route>
	                    </Switch>
					</section>
                    <Footer />
                </main>
            </Router>
        )
    }
}


export default hot(module)(App);

import React, { Component } from 'react';


export default class SignUp extends Component {

	componentDidMount() {
		document.getElementById('email').focus();
	}

	render() {
	
		return (
			<section className="flex-container">
				<section className="form-container">
					<h2 className="form-title">Sign In to Your Account</h2>
					<form action="" method="get" className="form">
						<div className="form-group">
							<input type="text" name="email" id="email" placeholder="Email" required />
						</div>
						<div className="form-group">
							<input type="password" name="password" id="password" placeholder="Password" required />
						</div>
						<div className="form-group">
							<input type="submit" value="Sign In" />
						</div>
					</form>
				</section>
			</section>
		);
	}
}


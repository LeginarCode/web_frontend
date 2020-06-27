import React, { Component } from 'react';


export default class SignUp extends Component {

	componentDidMount() {
		document.getElementById('fname').focus();
	}
	render() {

		return (
			<section className="flex-container">
				<section className="form-container">
					<h2 className="form-title">Begin Your Legal Investment Journey</h2>
					<form action="" method="get" className="form">
						<div className="form-group">
							<label htmlFor="fname">First Name</label>
							<input type="text" name="fname" id="fname" required />
						</div>
	
						<div className="form-group">
							<label htmlFor="lname">Last Name</label>
							<input type="text" name="lname" id="lname" required />
						</div>
	
						<div className="form-group">
							<label htmlFor="email">Email</label>
							<input type="text" name="email" id="email" required />
						</div>
	
						<div className="form-group">
							<label htmlFor="password">Password</label>
							<input type="password" name="password" id="password" required />
						</div>
	
						<div className="form-group">
							<label htmlFor="cpassword">Confirm Password</label>
							<input type="password" name="cpassword" id="cpassword" required />
						</div>
	
						<div className="form-group">
							<input type="submit" value="Register" />
						</div>
					</form>
				</section>
			</section>
		);
	}
}



import React, { Component } from 'react';


import wojak1 from '../img/wojak1.jpg';
import wojak2 from '../img/wojak2.jpg';

export default class CaseComponent extends Component {


	constructor(props) {
		super(props);

		// When Backend Set Up:
		// 	Query database for case data and update state
		// 	accordingly
	}


	render() {
		
		const { id } = this.props;

		return (
			<div className="case-container">
				<h1>{id}</h1>

				<div className="case-dashboard">
					<section className="graphic grid-cell">
						<img className="case-img" src={wojak1} alt="wojak" />
					</section>
					<section className="invest grid-cell">
						<h2>Invest</h2>
					</section>
					<section className="info-pane grid-cell">
						<h2>Info Pane</h2>
					</section>
					<section className="related grid-cell">
						<h2>Related</h2>
					</section>
				</div>
			</div>
		);
	}
}

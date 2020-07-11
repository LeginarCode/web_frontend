// Wrapper Functional Component for rendering an individual case

import React, {Component } from 'react';
import { useParams } from 'react-router-dom';

import SearchWidget from '../components/SearchWidget';
import CaseComponent from '../components/CaseComponent';

import '../styles/Case/case.scss';

export default function Case() {
	
	let { id } = useParams();

	return (
		<div className="case-wrapper">
			<div className="case-grid">
				<div className="row case-search-row">
					<SearchWidget />
				</div>
				<div className="row case-main-row">
					<CaseComponent id={id} />
				</div>
			</div>
		</div>
	);
}

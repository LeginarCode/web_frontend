import React, { Component } from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

import '../styles/search_widget.scss';

export default function SearchWidget() {

	focus = e => {
		document.getElementById('search-cases').focus();
	}

	return (
		<div className="search-widget-container widget-container">
			<div className="search-widget-flex widget-flex">
				<div className="icon-wrapper flex-item-wrapper" onClick={focus}>
					<FontAwesomeIcon icon="search" />
				</div>
				<div className="input-wrapper flex-item-wrapper">
					<input type="text" placeholder="Search" name="search-cases" id="search-cases" />
				</div>
			</div>
		</div>
	);
}

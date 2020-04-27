import React from 'react'

import '../styles/footer.scss';

export default function Footer() {
    return (
        <footer>
            <div className="container">
                { /* Grid Layout */}
                <div className="col">
                    <h1>Footer A</h1>
                    <ul>
                        <li>Thing A1</li>
                        <li>Thing A2</li>
                        <li>Thing A3</li>
                    </ul>
                </div>
                <div className="col">
                    <h1>Footer B</h1>
                    <ul>
                        <li>Thing B1</li>
                        <li>Thing B2</li>
                        <li>Thing B3</li>
                    </ul>
                </div>
                <div className="col">
                    <h1>Footer C</h1>
                    <ul>
                        <li>Thing C1</li>
                        <li>Thing C2</li>
                        <li>Thing C3</li>
                    </ul>
                </div>

            </div>
        </footer>
    )
}

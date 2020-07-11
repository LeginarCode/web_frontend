import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import '../styles/home.scss';

import showcase_img from '../img/temp_showcase_new.png';
console.log(showcase_img);

export default class Home extends Component {
    render() {
        return (
            <React.Fragment>
                {/* Showcase */}
                <section className="showcase">
                    <div className="container">
                        <div>
                            <h1>Legal Investment Made Easy</h1>
                            <p>
                                Lorem ipsum dolor sit amet, consectetur
                                adipiscing elit. Vestibulum non molestie ex.
                                Nulla nibh ex, pharetra pellentesque mollis ut,
                                malesuada ut velit. Cras tincidunt dictum leo,
                                at porta purus venenatis ac.{" "}
                            </p>
                            <Link to="/signup">Sign Up</Link>
                        </div>
                        <img src={showcase_img} alt="showcase image" />
                    </div>
                </section>
                <section className="section">
                    <div className="container">
                        <h1>This is a section</h1>
                        <p>
                            What stuff do we need to include on the landing page
                        </p>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipiscing
                            elit. Nulla mattis, eros et feugiat interdum, lectus
                            diam aliquet dui, vitae pulvinar eros dolor
                            convallis arcu. Aliquam vel nisl vitae tortor
                            iaculis fermentum. Aliquam sollicitudin enim vel
                            enim commodo venenatis. Mauris vitae mauris ut elit
                            ullamcorper hendrerit ac ac massa. Pellentesque
                            condimentum vestibulum nulla, ut sodales augue
                            fermentum at. Vivamus a leo rhoncus, vulputate erat
                            sit amet, consequat purus. Maecenas vitae massa
                            vestibulum elit condimentum mattis. Mauris tincidunt
                            risus et erat pretium, nec aliquam felis tempor. Ut
                            laoreet, erat vitae aliquam tempor, erat libero
                            ultrices nisi, consectetur pellentesque ex tortor
                            sed justo. In aliquam faucibus eros, quis
                            pellentesque mauris condimentum tempor. Proin vel
                            turpis libero. Sed interdum at mauris non fermentum.
                            Etiam id tortor id dui sodales imperdiet id vitae
                            velit. Pellentesque feugiat venenatis vulputate.
                        </p>

                        <p>
                            Suspendisse nisi sapien, porttitor ac fermentum sit
                            amet, molestie accumsan dolor. Pellentesque vitae
                            tellus convallis, semper est vitae, facilisis sem.
                            Vestibulum efficitur fringilla erat, et pretium
                            ipsum accumsan sit amet. Pellentesque bibendum
                            libero sed urna cursus scelerisque. Nunc nec lorem
                            nec sem venenatis tempus. Praesent arcu elit, rutrum
                            at ipsum eget, vulputate pulvinar odio. Duis sit
                            amet bibendum arcu, nec eleifend lorem.{" "}
                        </p>
                    </div>
                </section>
                <section className="section">
                    <div className="container">
                        <h1>We Can Have More Sections</h1>
                        <p>
                            With more text
                        </p>
                        <code>Or code</code>
                    </div>
                </section>
                <section className="section">
                    <div className="container">
                        <h1>And even more</h1>
                        <p>With grids</p>
                        <p>Too lazy to do a grid rn</p>
                    </div>
                </section>
            </React.Fragment>
        );
    }
}

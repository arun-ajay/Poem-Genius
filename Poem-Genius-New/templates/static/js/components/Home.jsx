import React, { Component } from 'react';

class Home extends Component {
  render() {
  	const toTextFile = function(){
	  	var text = document.getElementById("input").value;
	    text = text.replace(/\n/g, "\r\n");
	    var textFile = new Blob([text], { type: "text/plain"});
      return textFile;
  	}

    const retrievePoemLitDevice = function(){
      var textFile = toTextFile();
      var processedFile = APIClient.getPoemLitDevices(textFile);
	  	document.getElementById("input").value = processedFile.toString();
    }
    return (
      <div className="">
        <header id="navtop" className="container-fluid sticky-top">
          <nav class="navbar navbar-expand-md bg-white navbar-light">
            <a id="logo" class="navbar-brand" href="#">Poem Genius</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
             <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="collapsibleNavbar">
             <ul class="navbar-nav ml-auto">
               <li class="nav-item">
                 <a class="nav-link" href="#">Home</a>
               </li>
               <li class="nav-item">
                 <a class="nav-link" href="#analyzer">Analyzer</a>
               </li>
               <li class="nav-item">
                 <a class="nav-link" href="#about">About Us</a>
               </li>
             </ul>
            </div>
          </nav>
        </header>
        <section id="home"></section>
        <br></br>
        <section id="analyzer" className="container-fluid">
          <div className="row">
            <div className="col-md-12">
              <h1 className="text-center">Analyzer</h1>
            </div>
          </div>
          <div className="row">
            <div className="offset-md-1 col-md-5 form-group">
              <form className="col-md-12">
                <p className="text-center"><strong>Input</strong></p>
                <textarea id="input" className="col-md-12 form-control" rows="10"></textarea>
              </form>
            </div>
            <div className="col-md-5 form-group">
              <p className="text-center"><strong>Output</strong></p>
              <textarea id="output" className="col-md-12 form-control" rows="10"></textarea>
            </div>
          </div>
        </section>
        <br></br>
        <section id="about" className="container-fluid">
          <div className="row">
            <div className="col-md-12">
              <h1 className="text-center">About Us</h1>
            </div>
          </div>
        </section>
        <footer id="footer" className="container-fluid">
          <ul className="nav justify-content-center">
            <li class="nav-item">
                <a href="#" className="nav-link">Home</a>
            </li>
            <li class="nav-item">
                <a href="#analyzer" className="nav-link">Analyzer</a>
            </li>
            <li class="nav-item">
                <a href="#about" className="nav-link">About Us</a>
            </li>
          </ul>
        </footer>
      </div>
    );
  }
}



export default Home;

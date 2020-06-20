import React from 'react';
import { Card, Button, CardTitle, CardText, Row, Col  } from 'reactstrap';

import './Main.css'
import { Link } from 'react-router-dom';
const Example = (props) => {
  return (
    //   <div>
    // <form class="form-inline active-cyan-3 active-cyan-4">
    // <ion-icon name="search-outline"></ion-icon>
    // <input class="form-control form-control-sm mr-3 w-75" type="text"
    //   name="keyword"
    //   placeholder="Search"  aria-label="Search"
    //   value={this.state.keyword} 
    //   onChange={this.onInputChange } 
    // />
    // </form>
    // </div>
    <Row className="main-margin">
      <Col sm="4" >
        <Card body>
          <CardTitle align ="center"><h2>서울시 데이터</h2></CardTitle>
          <CardText align ="center">서울시 데이터 자세히 보기</CardText>
          <Link to="/Detailseouldata"><Button outline color="primary" size="lg" block align="center">
              Go </Button></Link>
        </Card>
      </Col>
      <Col sm="4">
        <Card body>
          <CardTitle  align ="center"><h2>경기 데이터</h2></CardTitle>
          <CardText  align ="center">경기도 데이터 자세히 보기</CardText>
          {/* <Button outline color="secondary" size="lg"> <Link to ="/Detailggdata">Go </Link></Button> */}
          <Link to="/Detailggdata"><Button outline color="primary" size="lg"  block align="center">
              Go </Button></Link>
        </Card>
      </Col>
      <Col sm="4">
        <Card body>
          <CardTitle align ="center"><h2>공공 데이터</h2></CardTitle>
          <CardText align ="center">공공 데이터 자세히 보기</CardText>
          {/* <Button outline color="secondary"  size="lg"><Link to ="/Detailspublicdata">Go </Link> </Button> */}
          {/* <CardLink href="/Detailspublicdata">Card Link</CardLink> */}
          <Link to="/Detailspublicdata"><Button outline color="primary" size="lg"  block align="center">
              Go </Button></Link>
        </Card>
      </Col>
    </Row>
    
    
  );
};

export default Example;
import React, { Component } from "react"
import axios from "axios"
import ContactInfo from './ContactInfo';
import { paginate } from '../data/Paginate';
import Pagination from './Pagination';
import { Table } from 'reactstrap';

import './Data.css';


class Detail extends Component {
  constructor(props){
    super(props)
  
  this.state = {
    
 
    users: [],
    keyword : '',

    
  }
}
handlePageChange = (page) => {
  this.setState({ currentPage: page }); // 페이지 수 클릭 시 현재 페이지 변경
}


onInputChange  = (e) => { // 2. input 태그의 값이 변경 될 때마다 this.state.keyword 값이 변경
  this.setState({
    keyword : e.target.value
  });
}
  componentDidMount() {
    axios.get('http://localhost:8013/seouldatadb').then(res =>{
      this.setState({users :res.data})
    })
  }
  

  render() {

    const mapToComponents = (data) => {
       data.sort(); 
      data = data.filter( 
        (users) => { 
          return users.category.toLowerCase() 
          .indexOf(this.state.keyword.toLowerCase()) > -1; 
        }
      ); 
      return data.map( 
        (users, i) => { 
          return (<ContactInfo users={users} key={i} />); 
        } 
      );
    }    
    return ( 
      
    <div>

      <form class="form-inline active-cyan-3 active-cyan-4">
      <ion-icon name="search-outline"></ion-icon>
      <input class="form-control form-control-sm mr-3 w-75" type="text"
        name="keyword"
        placeholder="Search"  aria-label="Search"
        value={this.state.keyword} 
        onChange={this.onInputChange } 
      />
      
       <i class="fas fa-search" aria-hidden="true"></i>
 </form>

 <Table borderless>
      <thead>
        <tr align="center">
         
          <th align="center">제공 기관</th>
          <th align="center">정보</th>
          <th align="center">URL</th>
        </tr>
        
      </thead>
     <tbody>
  
      {mapToComponents(this.state.users)}
      </tbody>
</Table>
{/* 
<Pagination
          itemsCount={itemsCount}
          pageSize={pageSize}
          currentPage={currentPage}
          onPageChange={this.handlePageChange}
        /> */}
    </div>
    );
    

  }
  
}


export default Detail;
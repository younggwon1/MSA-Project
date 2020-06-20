import React from 'react';
import axios from 'axios';
import Pagination from "react-js-pagination";
import NewsFeed  from './NewsFeed';
import ContactInfo from './ContactInfo';
import { Table } from 'reactstrap';
import './Data.css';


class Detailpublicdata extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      articlesDetails: [],
      activePage: 0 ,
      totalPages: null,
      itemsCountPerPage:null,
      totalItemsCount:null,
      keyword : ''
    };
    this.handlePageChange = this.handlePageChange.bind(this);
    this.fetchURL = this.fetchURL.bind(this);
  }

  fetchURL(page) {

    axios.get(`http://localhost:8013/seouldatadb/detail?location=%ea%b3%b5%ea%b3%b5%eb%8d%b0%ec%9d%b4%ed%84%b0&page=${page}&size=7`)
      .then( response => {

        const totalPages = response.data.totalPages;
        const itemsCountPerPage = response.data.size;
        const totalItemsCount = response.data.totalElements;

        this.setState({totalPages: totalPages})
        this.setState({totalItemsCount: totalItemsCount})
        this.setState({itemsCountPerPage: itemsCountPerPage})

        const results = response.data.content;

        const updatedResults = results.map(results => {

          var timestamp = new Date(results.pubDate)
          var dateString = timestamp.toGMTString()
          return {
              ...results, dateString
            }
          });

          this.setState({articlesDetails: updatedResults});
          console.log(updatedResults);
          console.log(this.state.activePage);
          console.log(this.state.itemsCountPerPage);

      }
    );
  }

componentDidMount () {
    this.fetchURL(this.state.activePage)
  }

handlePageChange(pageNumber) {
  console.log(`active page is ${pageNumber}`);
  this.setState({activePage: pageNumber})
  this.fetchURL(pageNumber)

  }
  onInputChange  = (e) => { // 2. input 태그의 값이 변경 될 때마다 this.state.keyword 값이 변경
    this.setState({
      keyword : e.target.value
    });
  }
populateRowsWithData = () => {
  const articleData = this.state.articlesDetails.map(article => {
      return <NewsFeed
          key = {article.id}
          category = {article.category}
          location = {article.location}
          url={article.url}
        />;
    });

    return articleData
  }

render(){
    const mapToComponents = (data) => {
        data.sort(); 
       data = data.filter( 
         (articlesDetails) => { 
           return articlesDetails.category.toLowerCase() 
           .indexOf(this.state.keyword.toLowerCase()) > -1; 
         }
       ); 
       return data.map( 
         (articlesDetails, i) => { 
           return (<ContactInfo articlesDetails={articlesDetails} key={i} />); 
         } 
       );
     } 

  return (
    <div >

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
 <Table hover>
      <thead>
        <tr align="center">
         
          <th align="center">제공 기관</th>
          <th align="center">정보</th>
          <th align="center">분류</th>
          <th align="center">URL</th>
        </tr>
        
      </thead>
     <tbody>
  
     {mapToComponents(this.state.articlesDetails)}
      </tbody>
</Table>

    {/* {this.populateRowsWithData()} */}
   
    <div className="d-flex justify-content-center">
      <Pagination
       hideNavigation
       activePage={this.state.activePage}
       itemsCountPerPage={this.state.itemsCountPerPage}
       totalItemsCount={this.state.totalItemsCount}
       pageRangeDisplayed={10}
       itemClass='page-item'
       linkClass='btn btn-light'
       onChange={this.handlePageChange}
       />
     </div>
     
    </div>
  );
}
}


export default Detailpublicdata;
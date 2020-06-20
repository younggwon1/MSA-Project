import React, { Component } from 'react';
import { getApis } from '../../util/APIUtils';
import "./MyApiList.css"
import TableDelete from './TableDelete'



export default  class MyApiList extends Component {
  
  constructor(props) {
    super(props);
    this.state = {
      apilistinfo: [],
    }
    this.loadApilist = this.loadApilist.bind(this);
  }
  loadApilist() {
    // console.log(this.props.username)
    let test = getApis(this.props.username, this.props.userport);
    // console.log(test)
    // console.log(this.props.userport)
    return test;
  }

  componentDidMount() {
    this.loadApilist().then(res => {
      // console.log(res);
      this.setState({
        apilistinfo: res
      })
    })
  }

  render() {
    // console.log("REDERING.........", this.state.apilistinfo);
    const apilistinfo = this.state.apilistinfo;
    const userkey = this.props.userkey;
    // console.log(userkey)
    return (
      <div className="col-md-12 ftco-animate">
        {apilistinfo && apilistinfo.map((table, index) => (
          <div className="container job-post-item p-4 d-block d-lg-flex align-items-center"  key={index}>
            <div className="one-third mb-4 mb-md-0">
              <div>
                <TableDelete 
                  tablename = {table.tableName}
                  userkey = {userkey}
                  userport =  {this.props.userport}
                >    
                </TableDelete>
              </div>
              <div className="job-post-item-header align-items-center">
                <span className="subadge">Open api table</span>
                <h2 className="mr-3 text-black"><a href={'http://' + table.url + '?key=' + userkey}>{table.tableName}</a></h2>
              </div>
              <div className="job-post-item-body d-block d-md-flex">
                <div className="mr-3"><span className="icon-layers" />등록일:{table.createTableTime} </div>
              </div>
              {/* <div class="one-forth ml-auto d-flex align-items-center mt-4 md-md-0">
            <a href="new-post.html" class="btn btn-primary py-3">상세보기</a>
        </div> */}
            </div>
          </div>
        ))}
      </div>
    );
  }
}


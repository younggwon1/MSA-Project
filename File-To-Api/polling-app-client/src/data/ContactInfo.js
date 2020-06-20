import React, { Component } from 'react';
import { Table } from 'reactstrap';

export default class ContactInfo extends Component {
    render() {
        return (
                
        <tr align="center">
          <td align="center">{this.props.articlesDetails.location}</td>
          <td align="center">{this.props.articlesDetails.category}</td>
          <td align="center">{this.props.articlesDetails.classificationInfo}</td>
          <td align="center"><a href={`${this.props.articlesDetails.url}`} target='_blank'> {this.props.articlesDetails.url}</a></td>
        </tr>
      
        );
    }
}

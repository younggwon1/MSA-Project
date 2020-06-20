import React, { Component } from 'react';
import { Table } from 'reactstrap';

export default class ContactInfo extends Component {
    render() {
        return (
                
           
        <tr align="center">
          <td align="center">{this.props.users.location}</td>
          <td align="center">{this.props.users.category}</td>
          <td align="center">{this.props.users.enrollmentInfo}</td>
          <td align="center">{this.props.users.modifyInfo}</td>
        </tr>
        );
    }
}

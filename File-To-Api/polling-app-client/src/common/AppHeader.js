import React, { Component } from 'react';
import {
  Link,
  withRouter
} from 'react-router-dom';
import './AppHeader.css';
import { Layout, Menu, Dropdown, Icon } from 'antd';
const Header = Layout.Header;

class AppHeader extends Component {
  constructor(props) {
    super(props);
    this.handleMenuClick = this.handleMenuClick.bind(this);
  }

  handleMenuClick({ key }) {
    if (key === "logout") {
      this.props.onLogout();
    }
  }

  render() {
    let menuItems;
    if (this.props.currentUser) {
      menuItems = [
        <Menu.Item key="/">
          <Link to="/">
            Home
              </Link>
        </Menu.Item>,
        <Menu.Item key="/data">
          <Link to="/data">
            DATA 찾기
            </Link>
        </Menu.Item>,
        <Menu.Item key="/open">
          <Link to="/upload">
            Open Api
           </Link>
        </Menu.Item>,
        <Menu.Item key="/store">
          <Link to="/store">
            DATA STORE
      </Link>
        </Menu.Item>,
        <Menu.Item key="/profile" className="profile-menu">
          <ProfileDropdownMenu
            currentUser={this.props.currentUser}
            handleMenuClick={this.handleMenuClick} />
        </Menu.Item>
      ];
    } else {
      menuItems = [
        <Menu.Item key="/">
          <Link to="/">
            home
            </Link>
        </Menu.Item>,
        <Menu.Item key="/data">
          <Link to="/data">
            DATA 찾기
          </Link>
        </Menu.Item>,
        <Menu.Item key="/open">
          <Link to="/login">
            Open Api
        </Link>
        </Menu.Item>,
        <Menu.Item key="/store">
          <Link to="/store">
            DATA STORE
          </Link>
        </Menu.Item>,

        <Menu.Item key="/login">
          <Link to="/login">Login</Link>
        </Menu.Item>,
        <Menu.Item key="/signup">
          <Link to="/signup">Signup</Link>
        </Menu.Item>
      ];
    }

    return (
      <Header className="app-header">
        <div className="container">
          <div className="app-title" >
            <Link to="/">FILE TO API</Link>
          </div>
          <Menu
            className="app-menu"
            mode="horizontal"
            selectedKeys={[this.props.location.pathname]}
            style={{ lineHeight: '64px' }} >
            {menuItems}
          </Menu>
        </div>
      </Header>
    );
  }
}

function ProfileDropdownMenu(props) {
  const dropdownMenu = (
    <Menu onClick={props.handleMenuClick} className="profile-dropdown-menu">
      <Menu.Item key="user-info" className="dropdown-item" disabled>
        <div className="user-full-name-info">
          {props.currentUser.name}
        </div>
        <div className="username-info">
          @{props.currentUser.username}
        </div>
      </Menu.Item>
      <Menu.Divider />
      <Menu.Item key="profile" className="dropdown-item">
        <Link to={`/users/${props.currentUser.username}`}>Profile</Link>
      </Menu.Item>
      <Menu.Item key="logout" className="dropdown-item">
        Logout
      </Menu.Item>
    </Menu>
  );

  return (
    <Dropdown
      overlay={dropdownMenu}
      trigger={['click']}
      getPopupContainer={() => document.getElementsByClassName('profile-menu')[0]}>
      <a className="ant-dropdown-link">
        <Icon type="user" className="nav-icon" style={{ marginRight: 0 }} /> <Icon type="down" />
      </a>
    </Dropdown>
  );
}


export default withRouter(AppHeader);
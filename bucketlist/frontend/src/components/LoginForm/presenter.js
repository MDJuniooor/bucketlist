import React from "react";
import PropTypes from "prop-types";

const LoginForm = (props, context) => (
  <div >
    <form
      onSubmit={props.handleSubmit}
      method="post"
    >
      <input
        type="text"
        placeholder="Username"
       
        onChange={props.handleInputChange}
        name="username"
        value={props.usernameValue}
      />
      <input
        type="password"
        placeholder="Password"
        
        onChange={props.handleInputChange}
        name="password"
        value={props.passwordValue}
      />
      <input
        type="submit"
        value="Log in"
      
      />
    </form>
  </div>
);

LoginForm.propTypes = {
  handleInputChange: PropTypes.func.isRequired,
  usernameValue: PropTypes.string.isRequired,
  passwordValue: PropTypes.string.isRequired,
  handleSubmit: PropTypes.func.isRequired,
};


export default LoginForm;

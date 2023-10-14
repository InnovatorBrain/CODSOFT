import React from 'react';
import InputGroup from 'react-bootstrap/InputGroup';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

const AddTask = ({ handleAddSubmit }) => {
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent the form from submitting by default
    handleAddSubmit(); // Call the provided handleAddSubmit function
  };

  return (
    <div className="TaskInputCont">
      <form onSubmit={handleSubmit}>
        <InputGroup className="mb-3">
          <InputGroup.Text id="basic-addon1">@</InputGroup.Text>
          <Form.Control
            placeholder="Title"
            aria-label="Title"
            aria-describedby="basic-addon1"
          />
        </InputGroup>
        <InputGroup>
          <InputGroup.Text>Note here</InputGroup.Text>
          <Form.Control
            as="textarea"
            aria-label="Note"
            placeholder="Text"
          />
        </InputGroup>
        <div className="buttons-cont">
          <label className="material-checkbox" htmlFor="checkboxId">
            <input type="checkbox" id="checkboxId" />
            <span className="checkmark"></span>
            Completed
          </label>
          <Button type="submit" variant="dark" className="button-i">
            Submit
          </Button>
        </div>
      </form>
    </div>
  );
};

export default AddTask;

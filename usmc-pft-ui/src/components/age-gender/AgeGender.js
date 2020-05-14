import React from "react";
import { Select, TextField, Typography } from "@material-ui/core";

import styles from "./AgeGender.module.scss";

const AgeGender = (props) => {
  return (
    <div className={styles.container}>
      <div className={styles.pickItem}>
        <Typography>Age:</Typography>
        <TextField
          id="age"
          name="age"
          type="number"
          required
          inputProps={{
            min: 17,
            max: 99,
            maxLength: 2,
          }}
        />
      </div>
      <div className={styles.pickItem}>
        <Typography>Gender:</Typography>
        <Select name="gender" defaultValue={"M"} native>
          <option value={"M"}>M</option>
          <option value={"F"}>F</option>
        </Select>
      </div>
      <div className={styles.pickItem}>
        <Typography>High Alt:</Typography>
        <Select name="high_alt" defaultValue={"False"} native>
          <option value={"False"}>No</option>
          <option value={"True"}>Yes</option>
        </Select>
      </div>
    </div>
  );
};

export default AgeGender;

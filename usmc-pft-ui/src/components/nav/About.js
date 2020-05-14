import React from "react";
import { Typography, Paper } from "@material-ui/core";

import styles from "./Nav.module.scss";

const fitnessLink = "https://www.fitness.marines.mil/pft-cft_standards17/";
const MCOLink =
  "https://www.marines.mil/News/Publications/MCPEL/Electronic-Library-Display/Article/2052205/mco-610013a-wch-2/";
const MARADMINLink =
  "https://www.marines.mil/News/Messages/MARADMINS/Article/1869148/forthcoming-change-to-the-physical-fitness-test-pft/";

const About = (props) => {
  return (
    <div className={styles.container} style={{ width: "75%" }}>
      <Paper elevation={3} style={{ width: "75%", padding: "30px" }}>
        <div className={styles.container} style={{ marginTop: "20px" }}>
          <Typography variant="body2">
            A simple PFT and CFT Calculator.
          </Typography>
        </div>
        <div style={{ marginTop: "30px" }}>
          <Typography variant="body2">
            Click the tabs above to navigate to the appropriate calculator, or
            access the calculator you want directly by using the following
            links:
          </Typography>
        </div>
        <div className={styles.container} style={{ marginTop: "20px" }}>
          <Typography variant="body2">
            PFT Calculator: <a href="/PFT">www.usmc-pft.com/PFT</a>
          </Typography>
          <Typography variant="body2" style={{ marginTop: "10px" }}>
            CFT Calculator: <a href="/CFT">www.usmc-pft.com/CFT</a>
          </Typography>
        </div>
        <div style={{ marginTop: "30px" }}>
          <Typography variant="h6">
            Is this an official USMC website?
          </Typography>
          <Typography variant="body2">
            No, this website is not affiliated with, or endorsed by, the USMC or
            any other government entity. It is a hobby website intended to
            provide a readily available means of calculating PFT/CFT scores.
          </Typography>
        </div>
        <div style={{ marginTop: "30px" }}>
          <Typography variant="h6">Are these calculators accurate?</Typography>
          <Typography variant="body2">
            The calculators are designed to match the accuracy of calculators
            available from official USMC sources (MCTIMS, MOL, etc), however,
            you should always double check your results against the official
            sources. If you believe one of the calculators is showing an
            incorrect result, please send an email to{" "}
            <a href="mailto: admin@usmcpft.com">admin@usmcpft.com</a>.
          </Typography>
        </div>
        <div style={{ marginTop: "30px" }}>
          <Typography variant="h6">How are the scores calculated?</Typography>
          <Typography variant="body2">
            Scores are calculated in accordance with the{" "}
            <strong>publicly</strong> available official documentation and score
            tables published by HQMC at{" "}
            <a href={fitnessLink}>fitness.marines.mil</a>, which are formalized
            in <a href={MCOLink}>Marine Corps Order 6100.13A W/CH 2</a>, and{" "}
            <a href={MARADMINLink}>MARADMIN 330/19</a>.
          </Typography>
        </div>
      </Paper>
    </div>
  );
};

export default About;

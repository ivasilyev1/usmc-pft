import React from 'react';
import {
  Button,
  IconButton,
  Paper,
  Tooltip,
  Typography,
} from '@material-ui/core';
import { Link } from 'react-router-dom';
import GitHubIcon from '@material-ui/icons/GitHub';

import styles from './Nav.module.scss';

const fitnessLink = 'https://www.fitness.marines.mil/pft-cft_standards17/';
const MCOLink =
  'https://www.marines.mil/News/Publications/MCPEL/Electronic-Library-Display/Article/2524537/mco-610013a-wch-3-cancels-mco-610013a-wch-2/';
const MARADMINLink =
  'https://www.marines.mil/News/Messages/MARADMINS/Article/1869148/forthcoming-change-to-the-physical-fitness-test-pft/';
const githubLink = 'https://github.com/ivasilyev1/usmc-pft';

const About = (props) => {
  return (
    <div className={styles.aboutContainer}>
      <Paper elevation={3} style={{ padding: '30px' }}>
        <div className={styles.git}>
          <Tooltip title='View Code'>
            <IconButton size='small' target='_blank' href={githubLink}>
              <GitHubIcon color='disabled' />
            </IconButton>
          </Tooltip>
        </div>
        <div className={styles.container} style={{ marginTop: '10px' }}>
          <Typography variant='body1'>
            <u>
              <strong>PFT and CFT Calculators</strong>
            </u>
          </Typography>
        </div>
        <div style={{ marginTop: '30px' }}>
          <Typography variant='body2'>
            Click the tabs above to navigate to the appropriate calculator, or
            access the calculator you want directly by using the following
            buttons:
          </Typography>
        </div>
        <div className={styles.buttonContainer}>
          <Button
            color='primary'
            type='submit'
            variant='contained'
            component={Link}
            to='/PFT'
          >
            PFT Calculator
          </Button>
          <Button
            color='primary'
            type='submit'
            variant='contained'
            component={Link}
            to='/CFT'
          >
            CFT Calculator
          </Button>
        </div>
        <div style={{ marginTop: '30px' }}>
          <Typography variant='h6'>
            Is this an official USMC website?
          </Typography>
          <Typography variant='body2'>
            No, this website is not affiliated with, or endorsed by, the USMC or
            any other government entity. It is a hobby website intended to
            provide a readily available means of calculating PFT/CFT scores.
          </Typography>
        </div>
        <div style={{ marginTop: '30px' }}>
          <Typography variant='h6'>Are these calculators accurate?</Typography>
          <Typography variant='body2'>
            The calculators are designed to match the accuracy of calculators
            available from official USMC sources (MCTIMS, MOL, etc), however,
            you should always double check your results against the official
            sources. If you believe one of the calculators is showing an
            incorrect result, please send an email to{' '}
            <a href='mailto: admin@usmcpft.com'>admin@usmcpft.com</a>.
          </Typography>
        </div>
        <div style={{ marginTop: '30px' }}>
          <Typography variant='h6'>How are the scores calculated?</Typography>
          <Typography variant='body2'>
            Scores are calculated based on the publicly available official
            documentation and score tables published by HQMC at{' '}
            <a href={fitnessLink}>fitness.marines.mil</a>, which are formalized
            in <a href={MCOLink}>Marine Corps Order 6100.13A W/CH 3</a>, and{' '}
            <a href={MARADMINLink}>MARADMIN 330/19</a>.
          </Typography>
        </div>
      </Paper>
    </div>
  );
};

export default About;

import React, { useState } from 'react';
import { WindowsExplorer, ReaderClosed } from '@react95/icons'; // Assuming Icons are imported from a dedicated file
import {TaskBar, List} from '@react95/core';
import {Modal} from '@react95/core'

const Taskbar = () => {
  const [first, toggleFirst] = useState(false);
  const [second, toggleSecond] = useState(false);

  const closeFirst = () => toggleFirst(false);
  const closeSecond = () => toggleSecond(false);

  return (
    <>
      {first && (
        <Modal
          icon={<WindowsExplorer variant="16x16_4" />}
          title="Help"
          closeModal={closeFirst}
          width="300"
          height="200"
        />
      )}
      {second && (
        <Modal
          defaultPosition={{ x: 50, y: 50 }}
          width="300"
          height="200"
          icon={<ReaderClosed variant="16x16_4" />}
          title="Restarting Game"
          closeModal={closeSecond}
        />
      )}
      <TaskBar
        list={
          <List>
            <List.Item icon={<ReaderClosed variant="32x32_4" />} onClick={() => toggleSecond(true)}>
              Restart
            </List.Item>
            <List.Item icon={<WindowsExplorer variant="32x32_4" />} onClick={() => toggleFirst(true)}>
              Help
            </List.Item>
          </List>
        }
      />
    </>
  );
};

export default Taskbar;

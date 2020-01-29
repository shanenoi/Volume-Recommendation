package org.shanenoi.recommendvolume;

import androidx.appcompat.app.AppCompatActivity;
import android.media.AudioManager;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    class VolumeController {

        AudioManager audioManager = (AudioManager) getSystemService(AUDIO_SERVICE);

        VolumeController() {
            assert audioManager != null;
        }

        int currentVolume() {
            return audioManager.getStreamVolume(AudioManager.STREAM_MUSIC);
        }

        int maxVolume() {
            return audioManager.getStreamMaxVolume(AudioManager.STREAM_MUSIC);
        }

        void setMediaVolumeLevel(float percent) {
            audioManager.setStreamVolume(
                    AudioManager.STREAM_MUSIC,
                    (int) (this.maxVolume() * percent / 100.0),
                    AudioManager.FLAG_SHOW_UI
            );
        }

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}

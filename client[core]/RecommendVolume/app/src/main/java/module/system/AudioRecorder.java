package module.system;

import android.media.MediaRecorder;

public class AudioRecorder {

    public MediaRecorder mediaRecorder = new MediaRecorder();

    public AudioRecorder() {
        mediaRecorder.setAudioSource(MediaRecorder.AudioSource.MIC);
        mediaRecorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);
        mediaRecorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);
    }

    public int startRecording(String path) {
        mediaRecorder.setOutputFile(path);
        try {
            mediaRecorder.prepare();
            mediaRecorder.start();
        } catch (Exception error) {
            return 1;
        }
        return 0;
    }

    public int stopRecording() {
        try {
            mediaRecorder.stop();
        } catch (Exception error) {
            return 1;
        }
        return 0;
    }

    public void reuse() {
        mediaRecorder.release();
    }

    public void close() {
        mediaRecorder.reset();
    }

}

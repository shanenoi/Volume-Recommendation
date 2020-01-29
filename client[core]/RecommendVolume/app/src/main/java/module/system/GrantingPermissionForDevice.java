package module.system;

import android.Manifest;
import android.app.Activity;
import android.content.Context;
import android.content.pm.PackageManager;

import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

public class GrantingPermissionForDevice {

    public String[] listPermission = {
            Manifest.permission.WRITE_EXTERNAL_STORAGE,
            Manifest.permission.READ_EXTERNAL_STORAGE
    };
    public Object context = this;

    public boolean checkPermission() {
        for (String s : listPermission) {
            if (
                    ContextCompat.checkSelfPermission(
                            (Context) context,
                            s
                    ) != PackageManager.PERMISSION_GRANTED
            ) {
                return false;
            }
        }
        return true;
    }

    public void requestPermissions() {
        int REQUEST_PERMISSION_CODE = 1000;
        ActivityCompat.requestPermissions(
                (Activity) context,
                listPermission,
                REQUEST_PERMISSION_CODE
        );
    }

}

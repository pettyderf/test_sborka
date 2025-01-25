unit_dir="/etc/systemd/system"

units=$(ls ${unit_dir}/foobar-*.service)
for unit in $units; do
    s_name=$(basename "$unit" .service | sed 's/^foobar-//')

    old_dir="/opt/misc/$s_name"
    new_dir="/srv/data/$s_name"
    
    systemctl stop "$unit"
    mv "$old_dir" "$new_dir"

    sed -i "s|$old_dir|$new_dir|g" "$unit"
    sed -i "s|/opt/misc/$s_name/foobar-daemon|/srv/data/$s_name/foobar-daemon|g" "$unit"

    systemctl daemon-reload
    systemctl start "$unit"
done
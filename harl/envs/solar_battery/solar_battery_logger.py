from harl.common.base_logger import BaseLogger


class SolarBatteryLogger(BaseLogger):
    def get_task_name(self):
        return self.env_args.get("scenario", "solar_battery")

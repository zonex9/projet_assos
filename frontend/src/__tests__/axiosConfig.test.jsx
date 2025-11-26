import axiosInstance from "./axiosconfig";

test("axios instance should be correctly configured", () => {
expect(axiosInstance.defaults.baseURL).toBe("[http://localhost:5000/v2](http://localhost:5000/v2)");
expect(axiosInstance.defaults.timeout).toBe(5000);
});
